#!/usr/bin/env python
import functools

int2 = functools.partial(int,base = 2)
print int2('100')
print int('100',base = 2)

