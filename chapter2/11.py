# -*- coding: utf-8 -*-

#確認方法
#cat hightemp.txt | tr "\t" " "
#sed -e "s/control+v押してtab/ /g" hightemp.txt
#expand -t 1 hightemp.txt

f = open("hightemp.txt", "r")

for line in f:
	print line.replace("\t", " ").strip()
