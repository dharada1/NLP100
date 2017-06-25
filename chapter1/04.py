# -*- coding: utf-8 -*-

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."

#,と.を除いてからスペースでsplitする
words_array = sentence.replace(",","").replace(".","").split(" ")

word_len_list = []

str_to_num_dic = {}

one_character_list = [1,5,6,7,8,9,15,16,19]

for i,word in enumerate(words_array):
	if i+1 in one_character_list:
		str_to_num_dic[word[0:1]] = i+1
	else:
		str_to_num_dic[word[0:2]] = i+1

print str_to_num_dic
print sorted(str_to_num_dic.items(), key=lambda x: x[1])