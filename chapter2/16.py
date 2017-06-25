# -*- coding: utf-8 -*-

#指定行数区切りでファイル分割するプログラム
#python 16.py hightemp.txt 4
#第一引数がファイル名、第二が行数.

#確認
#3行区切りでout.始まりのファイルに分割される
#split -l 3 hightemp.txt out.

import sys

file_name = sys.argv[1]
line_limit_number = int((sys.argv[2]))

#ファイル読み込みをして、分割し、リストgrouped_txt_listに格納
grouped_txt_list = []
with open(file_name) as f_in:
	line_count = 0
	group_count = 0

	for line in f_in.readlines():
		if line_count == 0:
			grouped_txt_list.append(line)
		else:
			grouped_txt_list[group_count] += line
		line_count += 1

		if line_count == line_limit_number:
			line_count = 0
			group_count += 1

#"入力ファイル名+.out-[連番]"という形式でリストの要素ごとに出力
for i,output_text in enumerate(grouped_txt_list):
	with open(file_name+".out-"+str(i), "w") as f_out:
		f_out.write(output_text)