# pythonEncryptor
A simple encryptor-like cypher I made as a hobby project when I first learned python, my first language in any programming. 
The program takes a key and message input through the console, then uses the key to "encrypt" the message.
Each symbol in the key is associated with a line in the "keys.txt" file, and each line is translated to a dictionary that has a one-to-one translation of every symbol.
The dictionaries then take turns translating each letter of the message. 
  
Example:
  key: secret
    a dictionary for each character is pulled, one labeled "s", one for "e", one for "c", one for "r", and one for "t".
  message: donuts are the best
    "d" is deciphered by dictionary "s", 
    "o" is deciphered by dictionary "e", 
    "n" is deciphered by dictionary "c", 
    "u" is deciphered by dictionary "r",
    "t" is deciphered by dictionary "e",
    "s" is deciphered by dictionary "t",
    and so forth, continuting the loop with the "s" dictionary.

The complexity comes in the length of the key word and the fact that someone trying to crack it wouldn't know the length or characters of that key. 
Though this is clearly not production quality, it was a fun experiment to piece out.
