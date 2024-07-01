from stuff import readlineSpecific
from radmodule import rainbowtext, colored, paragraph

####### Create New Key ########

yeet = input('key: ')
scrambleLetterList = []

symbols = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', '/','.',',','?','>','<','-','_','=','+','[',']','{','}','|','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',')','`','~', '\'','\\',' ',':',';']

for letter in yeet:
	index = symbols.index(letter) + 1
	ready = readlineSpecific('keys.txt', index)
	scrambleLetters = ''
	counter = 0
	for letter in ready:
		if counter < len(ready):
			scrambleLetters += ready[counter]
			counter += 1
	scrambleLetterList.append(scrambleLetters)

########## Create Translators #########

def translator(cualLetterSequence):
	symbols = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', '/','.',',','?','>','<','-','_','=','+','[',']','{','}','|','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',')','`','~', '\'','\\',' ',':',';']
	dictionary = {}
	counter = 0
	for symbol in symbols:
		dictionary[symbol] = cualLetterSequence[counter]
		counter+=1
	return dictionary

translateList = []

for string in scrambleLetterList:
	moo = translator(string)
	translateList.append(moo)

########### Scramble Message ##########

print('\nWhat message do you want to encrypt?\n'+colored('Message: ', 'blue'), end='')
yeetPut = paragraph(input(''))
scrambledMessage = ""

counter = 0
for letter in yeetPut:
	currentTranslator = translateList[counter]
	value = currentTranslator[letter]
	scrambledMessage += value
	if counter == len(translateList)-1:
		counter = 0
	else:
		counter += 1

########## Leave em with a goodbye #########
print(rainbowtext('\n'+scrambledMessage))
print(paragraph('\nCopy and paste that result (right-click and select copy, do not attempt ctrl-C) and send it to whoever, then give them this program to decrypt it.'))
