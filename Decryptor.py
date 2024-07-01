from stuff import readlineSpecific, doNothing
from radmodule import clear, colored

####### Create New Key ########

yeet = input('key: ')
scrambleLetterList = []

symbols = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', '/','.',',','?','>','<','-','_','=','+','[',']','{','}','|','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',')','`','~', '\'','\\',' ',':',';']

for letter in yeet:
	index = symbols.index(letter) + 1
	pizza = readlineSpecific('keys.txt', index)
	counter = 0
	demLetters = ''
	for thing in pizza:
		demLetters += pizza[counter]
		counter+=1
		if counter == len(pizza):
			break
	scrambleLetterList.append(demLetters)

########## Create Translator ##########

def translator(cualLetterSequence):
	symbols = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z', '/','.',',','?','>','<','-','_','=','+','[',']','{','}','|','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',')','`','~', '\'','\\',' ',':',';']
	dictionary = {}
	counter = 0
	for symbol in symbols:
		dictionary[cualLetterSequence[counter]] = symbols[counter]
		counter+=1
	return dictionary

translateList = []

for string in scrambleLetterList:
	moo = translator(string)
	translateList.append(moo)

######## Translate inputed message ########
daMess = input('\nWhat message are you trying to decrypt?\nCopy and paste the message to decrypt it. Right-click and select paste, do not attempt ctrl-V.\n'+colored('Message: ', 'blue'))

output = ''

counter = 0
for letter in daMess:
	currentTranslator = translateList[counter]
	value = currentTranslator[letter]
	output += value
	if counter == len(translateList)-1:
		counter = 0
	else:
		counter += 1

print(colored('\nThe Translation: ','blue')+output)

yes = input('\nPress enter if you want to respond with an encryption\n')
clear()
try:
	import Encryptor.__main__
except:
	doNothing()
