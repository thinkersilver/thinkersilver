project: myfirstapp
doc-image: ./images/gutenberg.png
doc-name: app_getting_started
doc-title: Publish Quick, Publish Often
package: appname0
---

# Getting Started

Markdown is a lightweight markup language for writing documents. It is lightweight, elegant and effective.  Dittio.  Is a markdown publishing system which generates a static blog from markdown documents and jupyter noteboks.



### Create a  new site

```bash
dittio new my_first_site
```

this create the following directory tree

```bash
.
├── assets
├── content
├── images
└── src
├── components
└── css
└── highlight.js
└── 8.4.0
└── styles

```


### Publish a jupyter notebook

Make sure that the first code block defines the project properties in the comments

```bash


#project: dittio
#package: dittio
#doc-name: dit_getting_started
#doc-title: Getting Started
#doc-image: ./images/gutenberg.png

print "Hello World"
import ditio
%matplotlib inline


```

*** the notebook will not export without these properties set ***


* ___project___: This is the name of your project
* __package__:   A project may consist of several packages
* __doc-name__:  The document file name
* __doc-title__: Title of the article. This will show up in your site index
* __doc-image__: This image will show above the prevew text in your site index


### Refresh site map

```
dittio index my_first_site

```

### Start the WebServer

```
dittio server my_first_site
```
The following code will do two things
* include the cell as a code block
* embed the chart as a png
```python

import pandas as pd;
df = pd.DataFrame({ "numbers": range(1,10) } )
df.head()
df.plot()
```
Adding the IGNORE directive will exclude code from being packaged.


```
#IGNORE
#FILE: example_1.py
print "Hello World"
```

![](/images/image_7_0.png)
Adding the DIST directive will package your notebook code using setuptools.
The settings file stores the properties of your project and can be used to configure setup tools