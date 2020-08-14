#!/usr/bin/env python3

from cryptography.fernet import Fernet

def readkey():
	file = open("key.key", "rb")
	global key
	key = file.read()
	file.close()

def get_data():
	choose = input("Enter file to encrypt here --> ")
	global choose_out
	choose_out = input("Enter file output name here --> ")
	file = open(choose, "rb")
	global data
	data = file.read()

def encrypt():
	crypt_key = Fernet(key)
	global crypt_data
	crypt_data = crypt_key.encrypt(data)

def write_encrypted():
	crypted_file = open(choose_out + ".crypt", "wb")
	crypted_file.write(crypt_data)

readkey()
get_data()
encrypt()
write_encrypted()





