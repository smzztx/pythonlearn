#!/usr/bin/env python
import os

print range(1,11)

l = []
for x in range(1,11):
	l.append(x*x)

print l

l1 = [x*x for x in range(1,11)]
print l1

l2 = [x*x for x in range(1,11) if x % 2 ==0]
print l2

l3 = [m + n for m in 'abc' for n in 'xyz']
print l3

print [d for d in os.listdir('.')]

l4 = ['Hello', 'World', 18, 'Apple', None]
print [s.lower() for s in l4 if isinstance(s,str)]
