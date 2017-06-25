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

noun_dict = {}
for result in results:
	if result["pos"] == "名詞":
		if noun_dict.has_key(result["surface"]):
			noun_dict[result["surface"]] += 1
		else:
			noun_dict[result["surface"]] = 1

for key, value in sorted(noun_dict.items(), key=lambda x:x[1], reverse=True)[:10]:
	print key, value