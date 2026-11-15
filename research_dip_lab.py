import glob, itertools, numpy as np, pandas as pd
import event_study as E
ev=pd.read_parquet(E.CACHE/"events.parquet")
days={p.split('/')[-1][:-8]:pd.read_parquet(p) for p in glob.glob(str(E.CACHE/"days/*.parquet"))}
COST=0.001
# path of closes after each event: rel[k] = close(day+k)/p10 - 1, k=0..15
def paths(e):
    out=[]
    for r in e.itertuples():
        d=days[r.sym]; i=d.index.get_loc(r.day); p10=d["p10"].iloc[i]
        c=d["close"].iloc[i:i+16].to_numpy()/p10-1
        out.append(np.pad(c,(0,16-len(c)),constant_values=np.nan))
    return np.array(out)
def trade(path,T,S,H):
    for k in range(min(H+1,16)):
        r=path[k]
        if np.isnan(r): return np.nan,k
        if (T and r>=T) or (S and r<=-S) or k==H: return r-COST,k
    return np.nan,H
def evalset(P,T,S,H):
    x=np.array([trade(p,T,S,H) for p in P]); r=x[:,0]; r=r[~np.isnan(r)]
    return dict(n=len(r),mean=r.mean(),med=np.median(r),win=(r>0).mean(),t=r.mean()/(r.std()/np.sqrt(len(r))),hold=np.nanmean(x[:,1]))
groups={"no-news gap DOWN":ev[(ev.gap<0)&(ev.why=="no company headline")],
        "news gap DOWN":ev[(ev.gap<0)&(ev.why!="no company headline")],
        "no-news gap DOWN 7%+":ev[(ev.gap<=-0.07)&(ev.why=="no company headline")]}
grid=list(itertools.product([0,.03,.05,.08,.12],[0,.05,.08,.12],[3,5,10,15]))
best={}
for name,e in groups.items():
    d=e[e.day<E.SPLIT]; v=e[e.day>=E.SPLIT]; Pd,Pv=paths(d),paths(v)
    res=[(T,S,H,evalset(Pd,T,S,H)) for T,S,H in grid]
    res.sort(key=lambda x:-x[3]["t"])
    print(f"\n== {name}: discovery n={len(d)}, validation n={len(v)}")
    print(" baseline hold 5d  disc", {k:round(v_,4) for k,v_ in evalset(Pd,0,0,5).items()}, "| val", {k:round(v_,4) for k,v_ in evalset(Pv,0,0,5).items()})
    for T,S,H,r in res[:5]:
        rv=evalset(Pv,T,S,H)
        print(f" target {T:.0%} stop {S:.0%} hold {H:2d}d | disc mean {r['mean']*100:+.2f}% med {r['med']*100:+.2f}% win {r['win']:.0%} t {r['t']:.1f} hold {r['hold']:.1f}d | VAL mean {rv['mean']*100:+.2f}% med {rv['med']*100:+.2f}% win {rv['win']:.0%} t {rv['t']:.1f}")
    allv=[evalset(Pv,T,S,H)["mean"] for T,S,H in grid]; alld=[r["mean"] for *_,r in res]
    print(f" all {len(grid)} exit combos: disc mean {np.mean(alld)*100:+.2f}% (min {np.min(alld)*100:+.2f}) | val mean {np.mean(allv)*100:+.2f}% (min {np.min(allv)*100:+.2f}, share positive {np.mean(np.array(allv)>0):.0%})")
    best[name]=res[0][:3]
# portfolio sim on $200
def portfolio(e,T,S,H,slots,start,end):
    e=e[(e.day>=start)&(e.day<end)].copy(); e["ag"]=e.gap.abs()
    bydate={d:g.sort_values("ag",ascending=False) for d,g in e.groupby("day")}
    cal=days["SPY"].index; cal=cal[(cal>=start)&(cal<end)]
    cash=200.0; pos=[]; curve=[]; ntr=0; wins=0
    for d in cal:
        for r in (bydate[d].itertuples() if d in bydate else []):
            if len(pos)>=slots: break
            if any(p["sym"]==r.sym for p in pos): continue
            eq=cash+sum(p["val"] for p in pos); stake=min(cash,eq/slots)
            if stake<5: break
            dd=days[r.sym]; i=dd.index.get_loc(d)
            pos.append(dict(sym=r.sym,i0=i,entry=dd["p10"].iloc[i],stake=stake,val=stake)); cash-=stake
        keep=[]
        for p in pos:
            dd=days[p["sym"]]
            if d not in dd.index: keep.append(p); continue
            i=dd.index.get_loc(d); ret=dd["close"].iloc[i]/p["entry"]-1; p["val"]=p["stake"]*(1+ret); k=i-p["i0"]
            if (T and ret>=T) or (S and ret<=-S) or k>=H:
                cash+=p["stake"]*(1+ret-COST); ntr+=1; wins+=ret>COST
            else: keep.append(p)
        pos=keep; curve.append(cash+sum(p["val"] for p in pos))
    c=pd.Series(curve,index=cal); yrs=len(c)/252
    spy=days["SPY"]["close"].reindex(cal); 
    return dict(end=round(c.iloc[-1],0),cagr=f"{(c.iloc[-1]/200)**(1/yrs)-1:+.0%}",maxdd=f"{(c/c.cummax()-1).min():.0%}",low=round(c.min(),0),trades=ntr,per_yr=round(ntr/yrs),win=f"{wins/max(ntr,1):.0%}",spy=f"{(spy.iloc[-1]/spy.iloc[0])**(1/yrs)-1:+.0%}")
print("\n== $200 account simulation (raw returns, 0.1% cost per round trip)")
for name in ["no-news gap DOWN","no-news gap DOWN 7%+"]:
    T,S,H=best[name]
    for slots in (2,4):
        print(name,f"T{T:.0%} S{S:.0%} H{H}d slots {slots}","| disc 2019-24",portfolio(groups[name],T,S,H,slots,pd.Timestamp("2019-01-01"),pd.Timestamp(E.SPLIT)),"| VAL 2025-26",portfolio(groups[name],T,S,H,slots,pd.Timestamp(E.SPLIT),pd.Timestamp("2027-01-01")))
