# -*- coding: utf-8 -*-

#確認
#paste col1.txt col2.txt

f2 = open("col1.txt", "r")
f3 = open("col2.txt", "r")

f4 = open("column_merged.txt", "w")

for zipped_array in zip(f2,f3):
	string_to_write = zipped_array[0].rstrip("\n") + "\t" + zipped_array[1].rstrip("\n")
	f4.write(string_to_write + "\n")