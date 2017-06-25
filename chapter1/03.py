# -*- coding: utf-8 -*-

sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

#,と.を除いてからスペースでsplitする
words_array = sentence.replace(",","").replace(".","").split(" ")

word_len_list = []

for word in words_array:
	word_len_list.append(len(word))

print word_len_list