name: dit_getting_started
title: Getting Started
date: 2018-01-06 14:47:41.416816
package: pkg_readme
assets: config.json,bin,setup.py,pkg_readme
---
# Getting Started

Markdown is a lightweight markup language for writing documents. It is lightweight, elegant and effective.  Dittio.  Is a markdown publishing system which generates a static blog from markdown documents and jupyter noteboks. 


##  Publish a notebook 

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