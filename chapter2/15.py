# -*- coding: utf-8 -*-

#python 15.py hightemp.txt 4
#第一引数がファイル名、第二が行数.

#確認
#tail -n 4 hightemp.txt

import sys

file_name = sys.argv[1]
line_number = int((sys.argv[2]))

with open(file_name) as f:
	new_list = []
	#"-line_number"の位置から最後までスライスしてる
	for line in f.readlines()[-line_number:]:
		print line.strip()
