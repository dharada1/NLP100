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

	#内部リンクの除去
	info_value = re.sub(ur'\[\[(.*?)(?:\]\]|\|.*?\]\]|\#.*\|.*?\]\])', r'\1', info_value)

	#<br/> or <br />除去
	info_value = re.sub(ur"(.*?)<br(/| /)>", ur"\1", info_value)

	#<ref>...</ref>除去
	ref = re.compile(ur"(.*?)<ref>(.*?)</ref>", re.DOTALL)
	info_value = re.sub(ref, ur"\1", info_value)

	#一個余ってる</ref>も削除
	info_value = re.sub(ur"</ref>","", info_value)

	#<ref name~>除去
	info_value = re.sub(ur"(.*?)<ref name.*?>", ur"\1", info_value)

	#{{ }}除去
	info_value = re.sub(ur"{{(.*?)}}", ur"\1", info_value)

	#リンク[ ]除去
	info_value = re.sub(ur"(.*?)\[.*?\]", ur"\1", info_value)

	print "-------------"
	print "key:"
	print info_key.encode("utf-8")
	print "value:"
	print info_value.encode("utf-8")


	basic_info_dict[info_key] = info_value
