#coding:utf-8

import urllib
import urllib2
import json

import re

f = open("UK.txt","r")
data = []

pattern1 = ur"\[\[(ファイル:|File:).*\]\]"

img_name = ""
for line in f:
	if "国旗画像" in line:
		img_name = line.split(" = ")[1].rstrip()
f.close()

print img_name

BASIC_PARAMETERS = {'action': 'query',
	'format': 'json',
	'prop': 'imageinfo',
	'iiprop': 'url'
	}

BASIC_PARAMETERS["titles"] = "File:" + img_name


URL = 'https://commons.wikimedia.org/w/api.php'
URL += "?{0}".format(urllib.urlencode(BASIC_PARAMETERS))
response = urllib2.urlopen(URL)
data = json.load(response)
print data['query']['pages']['347935']['imageinfo'][0]['url']
