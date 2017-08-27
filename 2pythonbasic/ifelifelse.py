#!/usr/bin/env python

age = raw_input('please enter your age: ')
age = int(age);
print age
if age >= 18:
	print 'adult'
elif age >=6:
	print 'teenager'
else:
	print 'kid'
