'''
=================================================================================================
R Cipher Suite
Includes all variants of the R cipher
=================================================================================================
Developed by: ProgramRandom, a division of RandomCorporations

A Page For This Project Will Be Created Soon On lakewood999.github.io

Visit my webpage at: https://lakewood999.github.io -- Note that this is my personal page, not the RandomCorporations page
=================================================================================================
What is the R cipher: This is just a random dipher that I came up with.  I will not say this is a good cipher, or perfect cipher, but it's just something I decided to make.  The R cipher is an improved version of the Caesar cipher

Root of the name: R cipher
-Well, cipher is just what it is, and R stands for random, or things being randomly generated
=================================================================================================
License:
You are free to use this script free of charge, however, I am not responsible for any types of problems caused by this script.  By using this program, you agree to not hold be liable for any charges related to this programe.
You are free to modify, and distribute this software(free of charge), but you are NOT allowed to commercialize this software(sell).  Please attribute this program to me if you are sharing it, or re-distributing it
=================================================================================================
Status:

This project is currently a WIP
-Variant "i" of the R cipher comping up

Version: Version 1: The X Update

R Cipher X - Progress: 100%
=================================================================================================
'''
import random

def letterout(x):
	out = ""
	x = str(x)
	if x == "1":
		out = "a"
	elif x == "2":
		out = "b"
	elif x == "3":
		out = "c"
	elif x == "4":
		out = "d"
	elif x == "5":
		out = "e"
	elif x == "6":
		out = "f"
	elif x == "7":
		out = "g"
	elif x == "8":
		out = "h"
	elif x == "9":
		out = "i"
	elif x == "10":
		out = "j"
	elif x == "11":
		out = "k"
	elif x == "12":
		out = "l"
	elif x == "13":
		out = "m"
	elif x == "14":
		out = "n"
	elif x == "15":
		out = "o"
	elif x == "16":
		out = "p"
	elif x == "17":
		out = "q"
	elif x == "18":
		out = "r"
	elif x == "19":
		out = "s"
	elif x == "20":
		out = "t"
	elif x == "21":
		out = "u"
	elif x == "22":
		out = "v"
	elif x == "23":
		out = "w"
	elif x == "24":
		out = "x"
	elif x == "25":
		out = "y"
	elif x == "26":
		out = "z"
	return out
#This is script just returns the number depnding on the input--WIP Need to alternate
def numberout(x):
	out = ""
	if x == "a":
		out = "1"
	elif x == "":
		out = "0"
	elif x == "b":
		out = "2"
	elif x == "c":
		out = "3"
	elif x == "d":
		out = "4"
	elif x == "e":
		out = "5"
	elif x == "f":
		out = "6"
	elif x == "g":
		out = "7"
	elif x == "h":
		out = "8"
	elif x == "i":
		out = "9"
	elif x == "j":
		out = "10"
	elif x == "k":
		out = "11"
	elif x == "l":
		out = "12"
	elif x == "m":
		out = "13"
	elif x == "n":
		out = "14"
	elif x == "o":
		out = "15"
	elif x == "p":
		out = "16"
	elif x == "q":
		out = "17"
	elif x == "r":
		out = "18"
	elif x == "s":
		out = "19"
	elif x == "t":
		out = "20"
	elif x == "u":
		out = "21"
	elif x == "v":
		out = "22"
	elif x == "w":
		out = "23"
	elif x == "x":
		out = "24"
	elif x == "y":
		out = "25"
	elif x == "z":
		out = "26"
	return out

def rcipherx(x):
	#This is script just returns the letter depnding on the input

	#This is the function that encrypts the text
	
	def encrypt(text):
		encrypted = ""
		key = ""
		totalscan = len(text)
		scan = 0
		while scan < totalscan:
			prekey = random.randint(1, 26)
			letter = text[scan]
			letternum = numberout(letter)
			encryptout = ""
			if letternum == "":
				encryptout = " "
				prekey = ""
			else:	
				lettersum = prekey+int(letternum)
				if lettersum > 26:
					lettersum = lettersum % 26
				encryptout = letterout(lettersum)
				
			
			if key != "":
				if prekey == "":
					key = key
				else:
					key = key + ", " + str(prekey)
			else:
				if prekey == "":
					key = key
				else:
					key = key + str(prekey)
			encrypted += encryptout 
			scan += 1
		print("Your encrypted message: "+encrypted)
		print("Here is your key: "+key)
		
	def decrypt(text):
		decrypted = ""
		key = input("What is the key(Key Numbers Must Be Separated By Commas With Spaces, e.g. 1, 2, 4): ")
		keylist = key.split(', ')
		print("Warning: Your key length must be equal to the number of characters in the text your are trying to decrypt, or this decryption will be unsuccessful")
		totalscan = len(text)
		scan = 0
		keyscan = 0
		while scan < totalscan:
			letter = text[scan]
			letternum = numberout(letter)
			decryptout = ""
			if letternum == "":
				decryptout = " "
				scan = scan +1
			else:
				decryptout = int(letternum) - int(keylist[keyscan])
				if decryptout < 0:
					decryptout = letterout(26-abs(decryptout))
				else:
					decryptout = letterout(decryptout)
				scan = scan + 1
				keyscan = keyscan+1
			decrypted += str(decryptout)
		print("Your decrpyted message is: "+decrypted)
		print("This message was decrypted with a key of: "+key)
	if x == "encrypt":
		encrypt(input("Please type in the text you would like to encrypt: "))
	elif x == "decrypt":
		decrypt(input("Please type in the text you would like to decrypt: "))
	#encrypt(input("Please type in the text you would like to encrypt: "))
	#decrypt(input("Please type in the text you would like to decrypt: "))
	
#rcipherx()
	
			
			
			








