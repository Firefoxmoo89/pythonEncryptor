from radmodule import *
from time import sleep

print(paragraph("Welcome to my Python Encryptor!"))
print(paragraph("This program was made by Christopher Beadle on replit using the python coding language. This program allows you to encrypt a message that can only be decoded with your special key! Feel free to look at any of the files to peek around and see how they work."))
input(paragraph("(Press Enter to Proceed)\n"))
clear()
print(paragraph("""If you would like...
 - To see a tutorial how to use the console in general, press "t" then "Enter"
 - An explanation of this program, then press "e" then "Enter"
 - To continue on to the program, just press "Enter" """))
maybe = validinput("",["t","e",""],extras="lower")
clear()

if maybe.lower() == "t":
	consoleTutorial()
elif maybe.lower() == "e":
	print(paragraph("You will be asked if you want to encrypt or decrypt. Choose encrypt if you want to create a secret message, and decrypt to read a secret message you have recieved."))
	sleep(1)
	print(paragraph("After choosing, you will be prompted for a key. This is a special keyword established for the specific message. If you are the encryptor, you get to choose what the key is to unlock the message you are about to write. If you are the decryptor, you need to know the key made by the encryptor in order to decode the message."))
	sleep(1)
	print(paragraph("After putting in the key, you will be asked for the secret message. If you are encrypting, this is your chance to write something up that will then be transformed. If you are decrypting, this is where you put the message you recieved to get it decrypted. To paste in the console, use \"ctrl+shift+v\""))
	sleep(1)
	print(paragraph("After putting in the secret message, either the encrypted or decrypted message should appear in fancy colors. To copy the message from the console, use \"ctrl+shift+c\""))
	sleep(1)
	input(paragraph("Press Enter to continue\n"))		

clear()
waiting = True
while waiting:
	start = intinput('''Do you want to:\n
1. Encrypt
2. Decrypt\n
	Select: ''')
	if start == 1:
		clear()
		import Encryptor
		waiting = False
	elif start == 2:
		clear()
		import Decryptor
		waiting = False
	else:
		print('you did not choose a valid option. Please try again.')
		sleep(2)
		clear()
