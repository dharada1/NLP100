#coding:utf-8

import json
import re

f = open("UK.txt","r")
data = []

pattern1 = ur"^=.*=$"

for line in f:
	section_search = re.search(pattern1, line)
	if section_search:
		section_string = section_search.group()
		section_level = section_string.count("=") / 2
		section_name = section_string.replace("=", "").strip()
		print section_name, section_level
f.close()
