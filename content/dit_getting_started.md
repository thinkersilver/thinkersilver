name: dit_getting_started
title: Getting Started
date: 2017-12-31 12:34:14.384598
package: pkg_readme
assets: config.json,bin,setup.py,pkg_readme
---

# Publish a notebook 

Create a new blog site.

``` bash 
dit site new  mynewsite 
```


Publish the notebook to the new site. 
```
dit publish $PYTHONNOTEBOOK mynewsite 
```

* export markdown 
* exports code 
* extracts images 
* stages posts in the blog folder 

Reindex. 


```
cd mynewsite 
dit site reindex

```

start the site 

```
dit site preview 

```


### Site Preview 

Should look something like this 


![](/images/site_preview.png)


###  Site Index 

![](/images/site_index.png)