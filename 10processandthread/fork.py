#!/usr/bin/env python
import os
print 'process (%s) start...' %os.getpid()
pid=os.fork()
if pid==0:
	print 'i am child process (%d) and my parent is %s' %(os.getpid(),os.getppid())
	print 'i (%s) just created a child process (%s).' %(os.getpid(),pid)
