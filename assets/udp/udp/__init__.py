#!/usr/bin/python
#package: udp
#name: udp
#title: Universal Dependency Manager (POC)
#INCLUDE
def store (__store__,f_hash,f_uri,f_contents):
    __store__[f_hash] = (f_uri,f_contents)
(b_in,b_out) = (("./ditio/**","setup.py","./bin/ditio","config.json"),"./dist/ditio-0.0.1-py2.7.egg")
op = "python setup.py bdist_egg"
__store__= {}
get_files= lambda pattern:  ("./ditio/test.py")
md5hash = lambda f : (f,"0x00")
content = lambda f : "Content"
transform = lambda b_in,b_out,operation :  ("proto://path/to/file", "hash 0x0", "output content")
    
for f in get_files("./ditio/**"): 
    (f_uri,f_hash) = md5hash(f)
    f_content = content(f)
    store(__store__,f_hash,f_uri,f_content)
    
(f_uri,f_hash,f_content) = transform(b_in,b_out,"python setup bdist_egg")
store(__store__,f_hash,f_uri,f_content)
# rule, you can only produce one artefact and that's it. 