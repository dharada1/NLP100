#coding:utf-8

import json
import time

f = open("jawiki-country.json","r")
data = []

for line in f:
	data.append(json.loads(line,"utf-8"))

#key（データ項目）の表示
print data[0].keys()
#[u'text', u'title']

#データ数の表示
print len(data)
#206

for datum in data:
	#イギリスに関するテキストの表示
	if "Category:" in datum['text']:
		print datum['title'].encode('utf-8')

	#if datum['title'] == u"イギリス":
	#	print datum['text'].encode('utf-8')

f.close()