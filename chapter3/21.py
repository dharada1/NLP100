#coding:utf-8

import json
import time

f = open("UK.txt","r")
data = []

for line in f:
	if "Category" in line:
		print line.rstrip()
f.close()