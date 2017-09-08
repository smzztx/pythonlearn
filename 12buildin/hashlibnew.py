#!/usr/bin/env python
import hashlib
md5=hashlib.md5('123456')
print md5.hexdigest()
sha1=hashlib.sha1()
sha1.update('how to use sha1 in')
print sha1.hexdigest()
sha1.update('python hashlib?')
print sha1.hexdigest()
def calc_md5(password):
	md5=hashlib.md5(password)
	return md5.hexdigest()


db = {
	'michael': 'e10adc3949ba59abbe56e057f20f883e',
	'bob': '878ef96e86145580c38c87f0410ad153',
	'alice': '99b1c2188db85afee403b1536010c2c9'
}
def login(user, password):
	md5_now=calc_md5(password)
	if(db[user]==md5_now):
		print 'true'
	else:
		print 'false'

if __name__=='__main__':
	login('michael','123456')
