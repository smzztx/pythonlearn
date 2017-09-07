#!/usr/bin/env python
import struct
print struct.pack('>I',10240099)
print struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')
with open('windows.bmp','r') as f:
	s=f.read(30)
	print s
	s1=struct.unpack('<ccIIIIIIHH',s)
	print s1
	print s1[0]
	if (s1[0]=='B' and s1[1]=='M')or(s1[0]=='B' and s1[1]=='A'):
		print 'this is a bmp file.'
		print '%d Bytes.'% s1[2]
		print '%d colors.'% s1[9]
	else:
		print 'not a bmp file.'
