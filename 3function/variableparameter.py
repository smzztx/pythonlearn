#!/usr/bin/env python
def calc(*numbers):
	sum = 0
	for n in numbers:
		sum = sum + n * n
	return sum
nums = [1,2,3]
print(calc(*nums))

nums = (2,3,4)
print(calc(*nums))

