# The user enters the tape. The program should take the last letter, and all the same letters from the tape. The result is displayed on the screen.

text = input(str('Enter words: '))
lastSymbol = text[-1]

new_text = ""

for lastSymbol in str(text):
	if lastSymbol == text[-1]:
		continue
	new_text = new_text + lastSymbol 

print (new_text)