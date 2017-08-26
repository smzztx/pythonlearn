#!/usr/bin/env python

class Student(object):
	def __init__(self,name,score):
		self.__name=name
		self.__score=score
	def print_score(self):
		print '%s:%s' % (self.__name,self.__score)
	def get_grade(self):
		if self.__score>=90:
			return 'A'
		elif self.__score>=60:
			return 'B'
		else:
			return 'C'

if __name__=='__main__':
	s1=Student('tx',100)
	s1.print_score()
	print s1.get_grade()
	#print s1.__name
