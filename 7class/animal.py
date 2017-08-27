#!/usr/bin/env python
class Animal(object):
	def run(self):
		print 'running'

class Dog(Animal):
	def run(self):
		print 'dog is running'
class Cat(Animal):
	pass

if __name__=='__main__':
	dog=Dog()
	dog.run()
