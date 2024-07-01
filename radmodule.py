from os import system, get_terminal_size
from time import sleep
########################################################
def clear():
	'''Same as system('clear') but easier to type
	clears the console of all text'''
	system('clear')
########################################################
def intinput(prompt):
	'''tests if input is integer or not
	if any single character is not a digit, the function will requre a re-input
	returns the inputed value to allow programmers use
	'prompt' parameter should be a string'''
	digits = '0123456789'

	def check(value):  
		for letter in value:  
			if letter not in digits:  
				return False
		return True

	a_number = False
	while not a_number:
		enter = input(prompt)
		a_number = check(enter)

		if a_number:
			return int(enter)
		else:
			clear()
			print(colored("You did not enter a valid number, please try again\n", 'red'))
########################################################
def validinput(prompt,options,inclusive=True,extras=None):
  """ Tests if input is a valid input
  "prompt" parameter should be a string, same as input(prompt)
  "options" parameter should be a list containing the responses available
  "inclusive" parameter is boolean, and determines whether to only accept
  options listed or to accept all except the options listed
  "extras" parameter will either 'lower' or 'upper' the input before
  comparing to options list"""

  def check(value,options):
    for item in options:
      if value == item:
        if inclusive: return True
        else: return False
    return False

  valid = False
  while not valid:
    enter = input(prompt)
    if extras == "lower": enter = enter.lower()
    elif extras == "upper": enter = enter.upper()
    valid = check(enter,options)
    if valid == False:
      print(" --- You did not enter a valid value, please try again. --- ")

  return enter
###################################################################################
def rainbowtext(string):
	'''returns entered string in an assortement of colors
	colors include red, yellow, green, cyan, blue, and magenta, in that order
	returns value, does not print it
	'string' parameter should be a string(obviously)'''
	newstring = ""
	colorlist = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
	colorspot = 0

	for letter in string:

		if colorspot == 6:
			colorspot = 0

		if letter == " ":
			newstring = newstring + letter

		else:
			color = colorlist[colorspot]
			coloredletter = colored(letter, color)
			newstring = newstring + coloredletter
			colorspot = colorspot + 1

	return newstring
########################################################
def deleteline():
	'''Deletes the previous printed line in console
	Does not return a value, just deletes the last line
	'length' parameter should be an integer'''
	jerry, notjerry = consoleSize()
	space = " "*jerry
	beginning = "\033["+str(notjerry)+"D"
	string = "\033[1A" + space+"\033[1A"
	print (string)
########################################################
def doNothing():
	'''Literally just does nothing. 
	Most often used to fill in the except block or in an if/else statement, whatever you want.'''
	print('',end='')
########################################################
def consoleSize():
	'''Literally just os.get_terminal_size but easier to type :)
	technically uses the default os.get_terminal_size(1)
	returns a tuple, just like os.get_terminal_size
	first item in tuple is columns, second item is rows'''
	return get_terminal_size()
########################################################
def paragraph(*string):
	'''Lets you print a paragraph that doesn't clip words at the end, but instead do it like a document, and make the words go to the next line to keep it together
	Returns text, not prints, so your syntax should be print(paragraph(''))
	'string' parameter should be a string, same as print function'''
	allDem = string
	string = ""
	for item in allDem:
		string = string+item
	
	jerry, notjerry = consoleSize()
	stringLen = len(string)
	numOfLines = stringLen // jerry
	linesList = []

	if string.find(' ') == -1:
		return string

	if numOfLines !=0:
		for i in range(numOfLines):
			if i == 0:
				start = 0
				end = jerry * (i+1)
			else:
				start = end+1
				end = start + jerry

			end_not_space = True
			while end_not_space:
				if string[end] == ' ':
					end_not_space = False
					line = string[start:end]
					linesList.append(line)
				else:
					end += -1		
		
		start = end+1
		end = -1
		line = string[start:end] + string[end]
		linesList.append(line)

	else:
		return string

	finalString = ''
	for item in linesList:
		finalString += item+'\n'
	return finalString
########################################################
def colorExamples(textOrBackground):
	'''prints the 255 available colors for the 'colored' function in this same 'radmodule' module.
	'textOrBackground' parameter should be a string that reads either text or background, and shows either the text colors or the background colors'''
	if textOrBackground.lower() == 'text':
		special = '\u001b[38;5;'
	elif textOrBackground.lower() == 'background':
		special = '\u001b[48;5;'
	else:
		print('\u001b[31m' + "TypeError: inputed 'textOrBackground' parameter is not a valid option")
	finalString = ''
	for i in range(256):
		number = str(i)
		string = special + number + 'm ' + number
		finalString += string + '\u001b[0m  '
	print(finalString)
########################################################
def colored(string, textcolor, background=None, bold=False, underline=False):
	'''Allows you to print a string to the console in different colors.

	Available easy colors :
		text and background - black, red, green, yellow, blue, magenta, cyan, and white (default)
		text only - each bright color, ex. bright black
	Extra colors (text and background):
		if you want to have a wider variety, use the 'colorExamples' function in this same 'radmodule' module, to see the 256 available numbers. input that number into the desired color parameter in this 'colored' function. 

	returns the final string, does not print it, so syntax should be print(colored(''))
	'string' parameter should be a string
	'textcolor' parameter should be a string or integer
	'background' parameter should be a string or integer 
	'bold' and 'background' parameters can be enabled with anything that isn't 'False' '''

	### Check types ###
	if type(string) != type(''):
		return '\u001b[31m' + "TypeError: inputed 'string' parameter is not a string"
	
	if type(textcolor) != type('') and type(textcolor) != type(0):
		return '\u001b[31m' + "TypeError: inputed 'textcolor' parameter is not an integer or string"

	if background != None:
		if type(background) != type('') and type(background) != type(0):
			return '\u001b[31m' + "TypeError: inputed 'background' parameter is not an integer or string"

	### Textcolor shtuff ###
	if type(textcolor) == type(0):
		number = str(textcolor)
		colorChange = '\u001b[38;5;' + number + 'm'

	elif type(textcolor) == type(''):
			
		color = textcolor.lower()

		if color == 'black':
			colorChange = '\u001b[30m'
		elif color == 'red':
			colorChange = '\u001b[31m'
		elif color == 'green':
			colorChange = '\u001b[32m'
		elif color == 'yellow':
			colorChange = '\u001b[33m'
		elif color == 'blue':
			colorChange = '\u001b[34m'
		elif color == 'magenta':
			colorChange = '\u001b[35m'
		elif color == 'cyan':
			colorChange = '\u001b[36m'
		elif color == 'white':
			colorChange = '\u001b[37m'
		elif color == 'bright black':
			colorChange = '\u001b[30;1m'
		elif color == 'bright red':
			colorChange = '\u001b[31;1m'
		elif color == 'bright green':
			colorChange = '\u001b[32;1m'
		elif color == 'bright yellow':
			colorChange = '\u001b[33;1m'
		elif color == 'bright blue':
			colorChange = '\u001b[34;1m'
		elif color == 'bright magenta':
			colorChange = '\u001b[35;1m'
		elif color == 'bright cyan':
			colorChange = '\u001b[36;1m'
		elif color == 'bright white':
			colorChange = '\u001b[37;1m'
		else:
			return '\u001b[31m' + "Error: inputed 'textcolor' parameter is not a valid option"

	### background shtuff ###

	if type(background) == type(0):
		number = str(background)
		colorChange += '\u001b[48;5;' + number + 'm'

	elif type(background) == type(''):
		if background == 'black':
			colorChange += '\u001b[40m'
		elif background == 'red':
			colorChange += '\u001b[41m'
		elif background == 'green':
			colorChange += '\u001b[42m'
		elif background == 'yellow':
			colorChange += '\u001b[43m'
		elif background == 'blue':
			colorChange += '\u001b[44m'
		elif background == 'magenta':
			colorChange += '\u001b[45m'
		elif background == 'cyan':
			colorChange += '\u001b[46m'
		elif background == 'white':
			colorChange += '\u001b[47m'
		else:
			return '\u001b[31m' + "Error: inputed 'background' parameter is not a valid option"

	### bold shtuff ###
	if bold != False:
		colorChange += '\u001b[1m'

	### bold shtuff ###
	if underline != False:
		colorChange += '\u001b[4m'

	return colorChange + string + '\u001b[0m'
########################################################
def consoleTutorial():
	print(paragraph("Anytime the program asks for some sort of input, you can type where the white box is. After you press enter, it will send it in to the program."))
	pizza = input(paragraph("Try it here!: "))
	print(paragraph("You just said: \"",pizza,"\"\n"))
	print(paragraph("See? That wasn't so bad! Programs will often ask questions you can answer, provide a list of options that you will choose by inputing the number, and more ways to get feedback from the user!"))
	input(paragraph("To get out of here, just press enter again and the program should resume as normal :)"))
	clear()