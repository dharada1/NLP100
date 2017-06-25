# -*- coding: utf-8 -*-

#typoglycemia
#スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
#それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
#ただし，長さが４以下の単語は並び替えないこととする．
#適当な英語の文
#を与え，その実行結果を確認せよ．

import random

def typoglycemia(input_string):
	words_array = input_string.split(" ")
	output_words_array = []
	for word in words_array:
		if len(word) <= 4:
			output_words_array.append(word)
		else:
			shuffled_word_array = random.sample(word[1:-1] ,len(word)-2)
			shuffled_word = word[0] + "".join(shuffled_word_array) + word[-1]

			output_words_array.append(shuffled_word)

	output_string = " ".join(output_words_array)
	return output_string

example_text = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

print typoglycemia(example_text)