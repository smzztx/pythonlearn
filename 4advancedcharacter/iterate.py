#!/usr/bin/env python
from collections import Iterable

l = [1,2,3,4,5]
t = (2,3,4,5,6)
d = {'b':1,'a':2,'c':3}

for n in l:
	print n

for n in t:
	print n

for key in d:
	print key

for value in d.itervalues():
	print value

#for k,v in d.iteriterms():space
for k, v in d.iteritems():
	print k,v

for ch in 'ABC':
	print ch

print isinstance('abc',Iterable)

for i, value in enumerate(['A','B','C']):
	print i, value

for x, y in [(1,1),(2,2),(3,3)]:
	print x,y


