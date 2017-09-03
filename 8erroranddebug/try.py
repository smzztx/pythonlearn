#!/usr/bin/env python
try:
	print 'try...'
	r=10/0
	print 'result:',r
except ZeroDivisionError, e:
	print 'except:',e
finally:
	print 'finally...'
print 'end'

def foo(s):
	n = int(s)
	return 10 / n

def bar(s):
	try:
		return foo(s) * 2
	except StandardError, e:
		print 'Error!'
		raise
def main():
	bar('0')
main()
