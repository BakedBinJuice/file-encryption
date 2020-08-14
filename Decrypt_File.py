#!/usr/bin/env python3

from cryptography.fernet import Fernet
import sys

def readkey():
	file = open("key.key", "rb")
	global key
	key = file.read()
	file.close()

def get_data():
	global choose
	choose = input("Enter file to decrypt here --> ")
	file = open(choose, "rb")
	global data
	data = file.read()

def decrypt():
	crypt_key = Fernet(key)
	global crypt_data
	crypt_data = crypt_key.decrypt(data)

def check_input():
	check = input("Would you like to add data to the file? (y/n) --> ")
	if (check == "y"):
		input_data()
	elif (check == "n"):
		pass
	else:
		print("That is not an option\nExiting...")
		sys.exit()

def input_data():
	global title
	global sub_title0
	global cred
	global sub_title1
	global cred0
	global sub_title2
	global cred1
	global sub_title3
	global cred2
	print("*ENTER CREDENTIAL TITLE IN ALL CAPS*")
	title = input("Enter title (ALL CAPS) here --> ")
	input_no = input("Enter number of inputs here (MAX 4) --> ")
	if (input_no == "1"):
		sub_title0 = input("Enter type of credential here --> ")
		cred = input("Enter credential here --> ")
		global data_set1
		data_set1 = (title + ":\n" + sub_title0 + ": " + cred + "\n")
		crypt_key = Fernet(key)
		#full_crypt_data = crypt_key.encrypt(data_set1)
		global dec_data
		dec_data = crypt_key.decrypt(data)
		new_decrypt_data = (str(dec_data) + "\n" + data_set1)
		show_new()


	elif (input_no == "2"):
		sub_title0 = input("Enter first type of credential here --> ")
		cred = input("Enter credential here --> ")
		sub_title1 = input("Enter second type of credential here --> ")
		cred0 = input("Enter credential here --> ")
		data_set2 = (title + ":\n" + sub_title0 + b": " + cred + b"\n" + sub_title1 + b": " + cred0 + b"\n")
		crypt_key = Fernet(key)
		full_crypt_data = crypt_key.encrypt(data_set2)
		crypt_data = crypt_data + full_crypt_data


	elif (input_no == "3"):
		sub_title0 = input("Enter first type of credential here -->")
		cred = input("Enter credential here --> ")
		sub_title1 = input("Enter second type of credential here --> ")
		cred0 = input("Enter credential here --> ")
		sub_title2 = input("Enter third type of credential here --> ")
		cred1 = input("Enter credential here --> ")
		data_set3 = (b(title + b":\n" + sub_title0 + b": " + cred + b"\n" + sub_title1 + b": " + cred0 + b"\n" + sub_title2 + b": " + cred1 + b"\n"))
		crypt_key = Fernet(key)
		full_crypt_data = crypt_key.encrypt(data_set3)
		crypt_data = crypt_data + full_crypt_data


	elif (input_no == "4"):
		sub_title0 = input(b"Enter first type of credential here -->")
		cred = input(b"Enter credential here --> ")
		sub_title1 = input(b"Enter second type of credential here --> ")
		cred0 = input(b"Enter credential here --> ")
		sub_title2 = input(b"Enter third type of credential here --> ")
		cred1 = input(b"Enter credential here --> ")
		sub_title3 = input(b"Enter fourth type of credential here --> ")
		cred2 = input(b"Enter credential here --> ")
		data_set4 = (title + b":\n" + sub_title0 + b": " + cred + b"\n" + sub_title1 + b": " + cred0 + b"\n" + sub_title2 + b": " + cred1 + b"\n" + sub_title3 + b": " + cred2 + b"\n")
		crypt_key = Fernet(key)
		full_crypt_data = crypt_key.encrypt(data_set4)
		crypt_data = crypt_data + full_crypt_data


	else:
		print(input_no + "credential inputs is not supported")

def write_new():
	file = open(choose, "wb")
	file.write(new_decrypt_data)

def show():
	for line in crypt_data.splitlines():
		print(line)

def show_new():
	for line in new_decrypt_data.splitlines():
		print(line)

readkey()
get_data()
check_input()
decrypt()
show()
print("\n")