#!/usr/bin/env python

def prime(n):
	x = 2
	while(x < n):
		if n % x == 0:
			return False 
		x = x + 1	
	return True
print filter(prime,range(2,100))
#print prime(20)
