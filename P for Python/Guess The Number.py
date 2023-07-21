#!/usr/bin/env python
#Coding_Resources
""" Guess the number game. Guess number in the range 1 to 100 """
__author__      = "Kaushik Chhappaniya"
__copyright__   = "Copyright 2023, Coding_Resources"

import random

def guess(number):
	trial_num = 1
	usr_input = -1
	while input != number:
		print("This is trial number:"+str(trial_num))
		usr_input = int(input("Enter number:\t"))
		if usr_input > number :
			print("Ohh you are far away from the right guess")
		elif usr_input < number :
			print("Ohh increase your guessed  number") 
		else :
			print("Yipiiee.. Right guess :)")
			exit()
		trial_num = trial_num + 1
	
if __name__ == "__main__":
	print("Let me guess any number from 1 to 100")
	number = random.randint(1,100)
	guess(number)
