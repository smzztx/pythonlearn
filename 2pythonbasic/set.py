#!/usr/bin/env python
s=set([1,2,3,4,5])
print s
set([1, 2, 3, 4, 5])

s.add(6)
print s
set([1, 2, 3, 4, 5, 6])

s.add(6)
print s
set([1, 2, 3, 4, 5, 6])

s.remove(6)
print s
set([1, 2, 3, 4, 5])

s1=set([3,5,7])
print s&s1
set([3, 5])

print s|s1
set([1, 2, 3, 4, 5, 7])
print s1-s

set([7])
print s^s1
set([1, 2, 4, 7])
