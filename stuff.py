from os import system
from time import sleep
############################################################################
def clear():
	'''bruh it just clears the console, same as system('clear')'''
	system('clear')
############################################################################
def filelen(filename):
	'''Returns the number of lines in a txt file that you input as 'filename' '''
	with open(filename) as daFile:
		counter = 1
		for line in daFile:
			counter += 1
	return counter
############################################################################
def fileclear(daFile):
	'''Clears your 'daFile' txt file'''
	yeet = open(daFile, 'w')
	yeet.close()
############################################################################
def newKey(writtenLine):
	'''Creates a new key into a txt file storage'''
	keptfile = 'lists.txt'
	tempfile = 'temp.txt'
	with open(keptfile, 'r') as readfile:
		with open(tempfile, 'w') as writefile:
			for i in range(filelen(keptfile)):
				readline = readfile.readline()
				writeline = writefile.write(readline)
			writefile.write('\n'+ writtenLine)
	with open(tempfile, 'r') as readfile:
		with open(keptfile, 'w') as writefile:
			for i in range(filelen(tempfile)):
				readline = readfile.readline()
				writeline = writefile.write(readline)
	fileclear(tempfile)
############################################################################
def filePrint(Filename):
	'''completely prints a file'''
	with open(Filename) as File:
		for line in File:
			print(line)
############################################################################
def fileSearch(fileadids, searchString):
	'''Searches for 'searchString' inputed string in 'fileadids' txt file
	returns the line number that your searchString is on'''
	with open(fileadids) as moo:
		fart = True
		countStuff = 1
		for line in range(filelen(fileadids)):
			while fart:
				chicken = moo.readline()
				cow = chicken.find(searchString)
				if cow == -1:
					if chicken == "":
						fart = False
						break
					fart = True
					countStuff += 1
				else:
					return countStuff
		return False
############################################################################
def readlineSpecific(daFile, lineNumber):
	'''same as readline function, but returns the specific line you want out of the file, which you choose with the 'lineNumber' parameter'''
	with open(daFile) as fileadids:
		for i in range(lineNumber):
			knife = fileadids.readline()
			if i + 1 == lineNumber:
				return knife
############################################################################
def doNothing():
	print('',end='')