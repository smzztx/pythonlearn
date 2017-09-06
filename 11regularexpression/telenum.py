#!/usr/bin/env python
import re
print 'please enter beijing tele number'
tele=raw_input()
if re.match(r'^\d{3}\-\d{3,8}$',tele):
	print 'ok'
else:
	print 'failed'

m=re.match(r'^(\d{3})\-(\d{3,8})$',tele)
print m.group(0)
print m.group(1)
print m.group(2)
