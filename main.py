import os
import sys
import wget
import random
import requests
import subprocess

from os  import *
from time import *
from  tqdm import *
from config import *

print ("Командная строка \nВсе права защищены ©")

sleep(1)

lang = input("Пожалуйста выберите язык/Please select a language (ru/eng) : ")

sleep(1)

if lang in langus:
	print("Загружаю...")
	sleep(1)
	os.system('cls||clear')

	mylist = [1,2,3,4,5,6,7,8,9,10]

	for i in tqdm(mylist):
		sleep(0.5)

	print ("Готово!")

	sleep(1)

	os.system('cls||clear')

	print(help)

	command = input ("Введите команду: ").lower()

	if command == 'git clone':
		url = input("Введите url: ")
		way = input("Введите путь: ")
		wget.download(url, way)

	elif command == 'help':
		print(help)

	elif command == 'start terminal':
		subprocess.Popen('C:\\Windows\\System32\\cmd.exe')

	elif command == 'exit':
		quit()



elif lang in langus_two:
	print("Loading...")
	sleep(1)
	os.system('cls||clear')

	mylist = [1,2,3,4,5,6,7,8,9,10]

	for i in tqdm(mylist):
		sleep(0.5)

	print ("Done!")

	sleep(1)

	os.system('cls||clear')

	print(help_two)

	command = input ("Type the command: ").lower()

	if command == 'git clone':
		url = input("Enter url: ")
		way = input("Enter way: ")
		wget.download(url, way)

	elif command == 'help':
		print(help_two)

	elif command == 'start terminal':
		subprocess.Popen('C:\\Windows\\System32\\cmd.exe')

	elif command == 'exit':
		quit()