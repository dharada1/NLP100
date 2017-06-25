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

for i in xrange(len(results)):
	if i > len(results) -2:
		break

	if results[i]["pos"] == "名詞" and results[i+1]["surface"] == "の" and results[i+2]["pos"] == "名詞":
		print results[i]["surface"] + results[i+1]["surface"] + results[i+2]["surface"]