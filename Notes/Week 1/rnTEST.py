# rnTEST.py

This is a TEST file to be used with doctest.
Generally, you will given a TEST file for
each hw, lab, and exam assignment.

IMPORTANT: everything must be named
EXACTLY the same as specified.  (ie. cAse sensitive)

>>> from reviewNamespaces import *

>>> match('b?b','bob')==True
True
>>> match('b?b','Bob')
False
>>> match('b?b','bobby')
False
>>> match('b??','ba')
False
>>> match('b??','baQ')
True



>>> allMatches('b?b','bob bad apple_fsdjk bib')==['bob','b b','bib']
True
