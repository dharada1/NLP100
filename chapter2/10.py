# -*- coding: utf-8 -*-

#確認方法
#wc -l hightemp.txt

f = open("hightemp.txt", "r")

for i,line in enumerate(f):
	pass

#iは0から始まってるので行数を数えるならi+1
print i+1