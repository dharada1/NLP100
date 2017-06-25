# -*- coding: utf-8 -*-

#python 14.py hightemp.txt 4
#第一引数がファイル名、第二が行数.

#確認
#head -n 4 hightemp.txt

import sys

with open(sys.argv[1]) as f:
	for line in f.readlines()[0:int(sys.argv[2])]:
		print line.strip()