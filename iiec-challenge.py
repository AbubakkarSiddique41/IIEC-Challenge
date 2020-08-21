#!/usr/bin/env python
# coding: utf-8
# Abubakkar Siddique
# Batch - 78

import os

def startt():
	with open(x, 'w') as file:
		pass
	os.system('notepad '+file.name)
	

def editt():
	data = input('Enter text to write into file : ')
	ff = open(x,'w')
	os.write(ff, data.encode())


def renamee():
	nn = input('Enter new name to the existing ' +x+ ' file (Without Extintion) : ')
	os.rename(x, nn+'txt')


def exitt():
	os.exit()


print('\n\nMenu Table :\n'+'-'*30)
print('1. Start Notepad\n2. Write to File\n3. Rename\n4. Exit\n')
x = 'Sample22.txt'
i = int(input('Select from above : '))
while True:
	if i == 1:
		startt()
	elif i == 2:
		editt()
	elif i == 3:
		renamee()
	elif i == 4:
		exitt()

	else:
		print('Enter valid number from above Menu.')


# In[ ]:




