#coding:utf-8
#カテゴリ名を正規表現で抽出する

import json
import re

f = open("UK.txt","r")
data = []

pattern1 = ur"\[\[Category:(.*?)\]\]$"
pattern2 = ur"\[\[Category:(.*?)\|.*?\]\]$"

for line in f:
	if "Category" in line:
		category_line = line.rstrip()
		category_name = re.search(pattern1, category_line).group(1)

		category_name = re.sub("\[\[Category:", "", category_name)
		category_name = re.sub("\]\]", "", category_name)
		if "|" in category_name:
			category_name = re.sub("\|", "", category_name)
			category_name = re.sub("\*", "", category_name)
		print category_name

f.close()