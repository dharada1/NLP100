#coding:utf-8

import re

f = open("UK.txt","r")

contents = f.read().decode("utf-8")
target = contents.split(u"基礎情報 国\n")[1].split("}}\n")[0]

target = target.replace('<references />\n', '')

#頭の|を削除してから
target = re.sub(ur'^\|', '', target)
#\n|でsplit
targets = re.split(ur"\n\|", target)

basic_info_dict = {}
for line in targets:
	key_and_value = line.split(" = ")
	print "-------------"
	print "key:"
	print key_and_value[0]
	print "value:"
	print key_and_value[1]

	basic_info_dict[key_and_value[0]] = key_and_value[1]
