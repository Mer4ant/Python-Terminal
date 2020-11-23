import os
import sys
import wget
import random
import smtplib
import requests
import subprocess

from os import  *
from time import *
from  tqdm import *
from config import *

# GO > GO > GO

os.system('cls||clear')

print ("Командная строка \nВсе права защищены © \nBy Mer4ant \nВыдавать себя как владелцем данного приложения запрещено \b*b<^>*")

print (mer)

sleep(1)

print (logo)

sleep(1)

print ("")

sleep(5)

os.system('cls||clear')

lang = input("Пожалуйста выберите язык/Please select a language (ru/eng) : ")

while True:

	sleep(1)

	if lang in langus:
		print("Загружаю...")
		sleep(0.5)
		os.system('cls||clear')

		mylist = [1,2,3,4,5,6,7,8,9,10]

		for i in tqdm(mylist):
			sleep(0.5)

		print ("Готово!")

		sleep(1)

		os.system('cls||clear')

		print(help)

		command = input ("$ ").lower()

		if command == 'git clone':
			url = input("Введите url: ")
			way = input("Введите путь: ")
			wget.download(url, way)

		elif command == 'help':
			print(help)

		elif command == 'start terminal':
			try:
			 os.startfile(r'C:\\Windows\\System32\\cmd.exe')
			except Exception as errorr:
				print("Ошибка!")

	#C:\\Windows\\System32\\cmd.exe

		elif command == 'sms bomber':
			nomer = input("Введите номер телефона: ")
			a = requests.post('https://eda.yandex.ru/api/v1/user/request_authentication_code',
				json = {"phone_number": nomer},)

		elif command == 'exit':
			quit()



	elif lang in langus_two:
		print("Loading...")
		sleep(0.5)
		os.system('cls||clear')

		mylist = [1,2,3,4,5,6,7,8,9,10]

		for i in tqdm(mylist):
			sleep(0.5)

		print ("Done!")

		sleep(1)

		os.system('cls||clear')

		print(help_two)

		command = input ("$ ").lower()

		if command == 'git clone':
			url = input("Enter url: ")
			way = input("Enter way: ")
			wget.download(url, way)

		elif command == 'help':
			print(help_two)

		elif command == 'start terminal':
			try:
				os.startfile(r'C:\\Windows\\System32\\cmd.exe')
			except Exception as error:
				print("Error!")

		elif command == 'sms bomber':
			nomer = input("Please enter number: ")
			a = requests.post('https://eda.yandex.ru/api/v1/user/request_authentication_code',
				json = {"phone_number": nomer},)

		elif command == 'exit':
			quit()