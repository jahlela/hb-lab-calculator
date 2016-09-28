"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


#explanation of how to quit & proper input / limitations on how many inputs

#prompt the user for an arithmetic function


#write a function to determine length of the input and repeats the operation n-2 times


#create a while loop
while True:
	input=raw_input("Enter an arithmetic statement, starting with the operator")
	tokens=input.split(" ")

	if tokens[0]=="q":
		break
	elif tokens[0]=="+":
		print add(tokens[1], tokens[2])
	elif tokens[0]=="-":
		print subtract(tokens[1], tokens[2])
	elif tokens[0]=="*":
		print multiply(tokens[1], tokens[2])
	elif tokens[0]=="/":
		print divide(tokens[1], tokens[2])
	elif tokens[0]=="**2":
		print square(tokens[1], tokens[2])
	elif tokens[0]=="**3":
		print cube(tokens[1], tokens[2])
	elif tokens[0]=="**":
		print power(tokens[1], tokens[2])
	elif tokens[0]=="%":
		print mod(tokens[1], tokens[2])



