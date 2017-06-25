#coding:utf-8

import re

def morph_analysis(file):
	f = open(file,"r")
	results = []
	for line in f:
		dict = {}
		items = re.split(r"\t", line.strip())
		if len(items) > 1:
			morph_info = items[1].split(",")
			dict["surface"] = items[0]
			dict["base"] = morph_info[6]
			dict["pos"] = morph_info[0]
			dict["pos1"] = morph_info[1]
			results.append(dict)
	return results

results = morph_analysis("neko.txt.mecab")

noun_list = []
for result in results:
	if result["pos"] == "名詞":
		noun_list.append(result["surface"])
	else:
		if len(noun_list) > 1:
			print "".join(noun_list)
		noun_list = []
