#!/usr/bin/env python
#throw the expection
import subprocess
import numpy as numpy
c='#abcdefgh'
print c.find('ab')
print len(c)
print c.find('ac')
print cmp(c,"#abcdefgh")
#nav = subprocess.Popen(["roslaunch", "amy_navigation", "amcl_nav.launch"])
#print nav
a = numpy.loadtxt("location.txt",delimiter=",")
print a
b=numpy.loadtxt("location1.txt",delimiter=",", dtype=float)
print b
print b.shape
print b[0]
with open('location1.txt', 'r') as f:  
	data = f.readlines()   
	print data	  
	loca = [[]]
	n = 0
	#print loca
	for line in data:  
		odom = line.split(',') 
		numbers_float = map(float, odom)
		print numbers_float
		if n ==0:
			loca = numbers_float
		else:
			loca = numpy.vstack((loca,numbers_float))
		#n1=0
		#for i in numbers_float:
		#	local[n][n1]=float[n1]
		#	n1=ni+1
		#loca[n][] = numbers_float
		n=n+1
		#loca = loca.append(numbers_float)
	print loca
