#!/usr/bin/env python
import rospy
import yaml

if __name__ == '__main__':
	#read the infomation from yaml file
	with open("route.yaml",'r') as stream:
		datamap=yaml.load(stream)
	print datamap
	print datamap[0]
	for obj in datamap:
		name = obj['filename']
		print "go to %s pose" % name[:-4]
		print obj['position']
		print obj['quaternion']

