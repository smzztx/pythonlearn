#!/usr/bin/env python

def name(n):
	return n.capitalize()

print map(name,['adam', 'LISA', 'barT'])

def prod(x,y):
	return x*y
print reduce(prod,[1,2,3,4])

