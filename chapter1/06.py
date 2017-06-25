# -*- coding: utf-8 -*-

def char_ngram(sentence, number):
	words_list = sentence.split(" ")

	char_ngram_list = []

	for word in words_list:
		for i in range(len(word) - 1):
			char_ngram_list.append( word[i:i+number] )

	return char_ngram_list

word1 = "paraparaparadise"
word2 = "paragraph"

#集合(set)としてそれぞれの単語のbi-gramを得る
#集合には重複がない
X = set(char_ngram(word1,2))
Y = set(char_ngram(word2,2))

print "X:"
print X

print "Y:"
print Y

print "和集合 X∪Y:"
print X.union(Y)

print "積集合 X∩Y:"
print X.intersection(Y)

print "差集合 X-Y:"
print X.difference(Y)

print "'se' in X:"
print 'se' in X

print "'se' in Y:"
print 'se' in Y