#!/usr/bin/python
#package: krt_getting_started
#name: README
#title: Getting Started
from krt import Graph
from krt.renderers import dot_render, display_graph
g = Graph.from_tuples([("a","b"),("c","d"),("c","d"),("c","b"),("d","e")])
dot_render(g)
import spacy
nlp = spacy.load("en")
s =  nlp(u"His speech caused a commotion, as audience members called out, both attacking and defending him.")
g  = Graph.from_tuples ( [ (t.head, t) for t in s  if t.pos_ not in [u'PUNCT']])
dot_render(g)