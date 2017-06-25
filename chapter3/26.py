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
	info_key = key_and_value[0]
	info_value = key_and_value[1]

	#強調部分の削除
	info_value = re.sub(ur'\'\'\'*(.*?)\'\'\'*', r'\1', info_value)

	print "-------------"
	print "key:"
	print info_key
	print "value:"
	print info_value


	basic_info_dict[info_key] = info_value
