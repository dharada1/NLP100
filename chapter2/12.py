# -*- coding: utf-8 -*-

#確認方法
#cat hightemp.txt | cut -f1,3
#cat hightemp.txt | cut -f1
#cat hightemp.txt | cut -f2

f1 = open("hightemp.txt", "r")

f2 = open("col1.txt", "w")
f3 = open("col2.txt", "w")

for line in f1:
	line_splitted_array = line.split("\t")

	f2.write(line_splitted_array[0] + "\n")
	f3.write(line_splitted_array[1] + "\n")

f1.close
f2.close
f3.close
