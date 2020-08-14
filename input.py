#!/usr/bin/env python3

from cryptography.fernet import Fernet 

def readkey():
	file = open("key.key", "rb")
	global key
	key = file.read()
	file.close()

def get_data():
	file = open("Test.crypt", "rb")
	global data
	data = file.read()
	file.close()

def decrypt():
	crypt_key = Fernet(key)
	global old_crypt_data
	old_crypt_data = crypt_key.decrypt(data)

def input_data():
	global input_string
	input_string = b"This is a test"

def encrypt():
	new_data = (old_crypt_data + b"\n" + new_decrypt_data)
	crypt_key = Fernet(key)
	global full_crypt_data
	full_crypt_data = crypt_key.encrypt(new_data)

def encrypt_new():
	crypt_key = Fernet(key)
	global new_encrypt_data
	new_encrypt_data = crypt_key.encrypt(input_string)

def decrypt_new():
	crypt_key = Fernet(key)
	global new_decrypt_data
	new_decrypt_data = crypt_key.decrypt(new_encrypt_data)

def new_crypt():
	file = open("Test.crypt", "wb")
	file.write(full_crypt_data)

def print_decrypt():
	crypt_key = Fernet(key)
	global final_decrypt_data
	final_decrypt_data = crypt_key.decrypt(full_crypt_data)
	print(final_decrypt_data)

readkey()
get_data()
decrypt()
input_data()
encrypt_new()
decrypt_new()
encrypt()
new_crypt()
print_decrypt()