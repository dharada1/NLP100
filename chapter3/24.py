#coding:utf-8

import json
import re

f = open("UK.txt","r")
data = []

pattern1 = ur"\[\[File:.*\]\]"

for line in f:
	media_search = re.search(pattern1, line)
	if media_search:
		media_string = media_search.group()
		print media_string.split("|")[0].lstrip("[[File:")
f.close()