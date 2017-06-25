#coding:utf-8

import json
import time

f = open("jawiki-country.json","r")
data = []

for line in f:
	data.append(json.loads(line,"utf-8"))

for datum in data:
	#イギリスに関するテキストの表示
	if datum['title'] == u"イギリス":
		print datum['text'].encode('utf-8')
f.close()

#python 20.py > UK.txt