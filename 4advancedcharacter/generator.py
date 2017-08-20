#!/usr/bin/env python

g = (x * x for x in range(1,11))
print g
for n in g:
	print n

def fib(max):
	n,a,b = 0,0,1
	while n<max:
		print b
		a,b,n = b,a+b,n+1

print fib(6)

def fib1(max):
	n,a,b = 0,0,1
	while n<max:
		yield b
		a,b,n = b,a+b,n+1

for n in fib1(6):
	print n



