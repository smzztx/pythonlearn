#!/usr/bin/env python
import sys
import os
print [x for x in os.listdir('.')]
def find_all():
	args=sys.argv
	if len(args)<=1:
		print 'please input name to search'
	else:
		find_dir(args[1])
def find_dir(name,dir='.'):
	if dir=='.':
		dir =os.path.abspath('.')
	print 'dir=%s'%dir
	for x in os.listdir(dir):
		if os.path.isdir(x):
			tmpdir=os.path.join(dir,x)
			find_dir(name,tmpdir)
		elif x.find(name)!=-1:
			print os.path.join(dir,x)

if __name__=='__main__':
	find_all()
