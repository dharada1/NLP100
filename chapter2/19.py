# -*- coding: utf-8 -*-

#各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．
#確認にはcut, uniq, sortコマンドを用いよ．
#LC_ALL=C cat hightemp.txt | cut -f1 | sort | uniq -c | sort -r

import sys
file_name = sys.argv[1]

with open(file_name, "r") as f:
	#県名を取り出しリストに格納
	prefecture_list = []
	for line in f:
		prefecture_list.append(line.split()[0])

	#県名をキー、出現数をバリューとする辞書を作成
	prefecture_count_dict = {}
	for prefecture in prefecture_list:
		if prefecture not in prefecture_count_dict:
			prefecture_count_dict[prefecture] = 1
		else:
			prefecture_count_dict[prefecture] += 1

	#辞書をバリューでソートして出力
	for k, v in sorted(prefecture_count_dict.items(), key=lambda x:x[1], reverse=True):
		print k, v