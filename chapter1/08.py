# -*- coding: utf-8 -*-

#aは97,zは122なので219-97=122(a=>z)
#また逆は219-122=97(z=>a)
#同様にb=>y y=>b, c=>x x=>c のようになる

def cipher(string):
	output_string = ""

	for character in list(string):
		if character.islower():
			output_string += chr( 219 - ord(character) )
		else:
			output_string += character

	return output_string


string = "Hello I am Daichi."

#暗号化
print cipher(string)

#暗号化して複合化
print cipher(cipher(string))
