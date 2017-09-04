#!/usr/bin/env python
import subprocess
import numpy as numpy
c='#abcdefgh'
print c.find('ab')
print len(c)
print c.find('ac')
#nav = subprocess.Popen(["roslaunch", "amy_navigation", "amcl_nav.launch"])
#print nav
a = numpy.loadtxt("location.txt",delimiter=",")
print a
