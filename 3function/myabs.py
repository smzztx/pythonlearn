#!/usr/bin/env python

x = int(raw_input('please enter a integer: '))

def my_abs(x):
	if x >=0:
		return x
	else:
		return -x
x = my_abs(x)
print x
