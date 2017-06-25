# -*- coding: utf-8 -*-
#1列目の文字列の種類（異なる文字列の集合）を求めよ．
#使い方
#python 17.py hightemp.txt

#確認方法
#cat hightemp.txt | cut -f1 | sort | uniq
#cat hightemp.txt | cut -f1 | sort | uniq | wc -l

import sys
file_name = sys.argv[1]

with open(file_name, "r") as f:
	col1_list = []
	for line in f:
		line_splitted_array = line.split("\t")
		col1_list.append(line_splitted_array[0])

	#setすることで重複無くなる.　要素数は len(set(col1_list)) でわかる。
	for col1 in set(col1_list):
		print col1
