#!/usr/bin/env python3

from cryptography.fernet import Fernet

def gen_key():
	global key
	key = Fernet.generate_key()

def write_key(key):
	file = open('key.key', 'wb')
	file.write(key)
	file.close

gen_key()
write_key(key)

