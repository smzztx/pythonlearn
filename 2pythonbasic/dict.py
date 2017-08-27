#!/usr/bin/env python
d={"chen":60,"zhang":80}
print(d)

d['chen']=65
print(d)

print(d.get("liu",0))

d['liu']=85
print(d)
d.pop('liu')
print(d)

print(d.keys())
print(d.values())

d1={'a':100,'b':99}
d.update(d1)
print(d)
