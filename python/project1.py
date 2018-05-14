import random

chars = 'abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#%^&*$?<>:;~'

pnum = input('How many passwords do you need to generate?')
pnum = int(pnum)
length = input('Input password length?')
length = int(length)


for p in range (pnum):
	password = ''
	for c in range(length):
		password += random.choice(chars)
	print(password)