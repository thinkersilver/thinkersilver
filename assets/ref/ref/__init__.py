#!/usr/bin/python
#package: ref
#name: ref
#title: Ref:  Swiss Army Knife for slicing arrays and dicts 
access = lambda m,k: {dict:lambda : m[k], 
                      list: lambda :m[k]
                          
                          
                    }
path_f = lambda m,keys : access(m,keys[0])[type(m)]() if len(keys) == 1 else path_f(access(m,keys[0])[type(m)](),keys[1:])  
value = lambda m,k : m[k] if k in m else None 
arr = lambda v :  v if type(v) in (list,set,tuple) else [v]
#path = lambda data,keys :  map(lambda m :  m[keys[0]] if len(keys) == 1 else path(m[keys[0]],keys[1:]), arr(data)  ) 
path = lambda data,r :  map(lambda m :  m[reffer(r)[0]] if len(reffer(r)) == 1 else path(m[reffer(r)[0]],reffer(r)[1:]), arr(data)  )  if  reffer(r)[0].isdigit() is False else  path(data[int(reffer(r)[0])],  reffer(r)[1:]) 
keys = lambda m,keys : m[keys[0]].keys()
typef = lambda m,keys :  type(path(m,keys))
reffer =  lambda r : r  if type(r) in [set,tuple,list] else r.split("/")
#Index 
#index = lambda items,k : dict([ (i[k],i) for i in items ])
indexff = lambda items,k,fn0,fn1 : dict([ (fn0(i,k),fn1(i)) for i in items ]) 
indexf = lambda items,k,fn : dict([ (fn(i,k),i) for i in items ])
index = lambda items,k:  indexf(items,k, lambda i,k: i[k])
view = lambda m,keys:  dict([(k,v) for  k,v in m.items() if k in keys])
#indexpath 
#indexpath = <----
#INCLUDE
import requests 
r = requests.get("http://api.nobelprize.org/v1/prize.json")
data = r.json() 
print path(data,"prizes")[0][0]
path(data,"prizes")[0][1]
#INCLUDE
view( 
    path(data,"prizes")[0][1], 
    ["category","laureates"]
#INCLUDE 
index(
    path(noise,["noiseprofiles"]),
    "maker"
# generate a performance heatmap
indexf(
    path(noise,["noiseprofiles"]),
    "maker",
    lambda i,k: i[k]
    
indexff(
    path(noise,["noiseprofiles"]),
    "maker",
    lambda i,k: i[k],
    lambda i: view(i,"models") 