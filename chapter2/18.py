# -*- coding: utf-8 -*-
#各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
#確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．

#使い方
#python 17.py hightemp.txt

#確認方法
#cat hightemp.txt | cut -f3 | sort

import sys
file_name = sys.argv[1]

with open(file_name, "r") as f:
	res=[]
	for line in f:
		res.append(line.split())

	#いくつかの要素から成る対象をキー指定してソートする
	for items in sorted(res, key=lambda x: x[2], reverse=True):
		print "\t".join(items).strip()