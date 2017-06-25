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

with open(file_name) as f:
	line_count = 0
	for line in f.readlines():
		print line.strip()
		line_count += 1

		if line_count == line_limit_number:
			print "------------------------"
			line_count = 0
