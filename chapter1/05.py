# -*- coding: utf-8 -*-

def word_ngram(sentence, number):
	words_list = sentence.split(" ")

	word_ngram_list = []

	for i in range(len(words_list) - 1):
		word_ngram_list.append( words_list[i:i+number])

	return word_ngram_list

def char_ngram(sentence, number):
	words_list = sentence.split(" ")

	char_ngram_list = []

	for word in words_list:
		for i in range(len(word) - 1):
			char_ngram_list.append( word[i:i+number] )

	return char_ngram_list

sentence = "I am an NLPer"

print word_ngram(sentence,2)
print char_ngram(sentence,2)