#!/usr/bin/env python
from types import MethodType
class Student(object):
	__slots__=('name','score')
s=Student()
s.name='micheal'
print s.name
def set_age(self,age):
	self.age=age
s.set_age=MethodType(set_age,s,Student)
s.set_age(25)
print s.age
s2=Student()
#print s2.age
def set_score(self,score):
	self.score=score
Student.set_score=MethodType(set_score,None,Student)
s.set_score(100)
print s.score
s2.set_score(99)
print s2.score
