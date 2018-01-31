name: ref
title: Ref:  Swiss Army Knife for slicing arrays and dicts
date: 2018-01-27 13:49:49.426817
package: ref
assets: config.json,ref,MANIFEST.in,bin,setup.py
---


![](/images/general_200.gif)
Ref is swiss army knife for slicing, selecting properties from nested document structures. 
Structures are keys using a __reference__ which is a list of keys.  e.g

```
{"name":"Bob", "surname":"Smith"}
```

The value "Bob" is accessed using the key "name" 

```
path({"name":"Bob", "surname":"Smith"},["name"]) 
```

This doesn't give us much over 

```python 

{"name":"Bob", "surname": "Smith"} ["name"] 

```

Let's look at a more complex example. 


	```
	
	import requests 
	r = requests.get("http://api.nobelprize.org/v1/prize.json")
	data = r.json() 
	print path(data,"prizes")[0][0]
	```

Let's  extract the categories and laureates from the first row 

	```
	view( 
	    path(data,"prizes")[0][1], 
	    ["category","laureates"]
	)
	```

## Index 


	```
	index(
	    path(noise,["noiseprofiles"]),
	    "maker"
	)
	
	# generate a performance heatmap
	
	indexf(
	    path(noise,["noiseprofiles"]),
	    "maker",
	    lambda i,k: i[k]
	    
	)
	
	indexff(
	    path(noise,["noiseprofiles"]),
	    "maker",
	    lambda i,k: i[k],
	    lambda i: view(i,"models") 
	)
	```

