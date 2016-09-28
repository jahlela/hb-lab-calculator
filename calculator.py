"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


#explanation of  limitations on how many inputs

#Explain how to quit & proper input format 
print "For each arithmetic statement, please start with the operator. Enter q at any time to quit. "

#write a function to determine length of the input and repeats the operation n-2 times


#create a while loop
while True:
	#Prompt the user for an arithmetic function and save input 
	input=raw_input("Enter a statement > ")
	tokens=input.split(" ")

	if tokens[0] == "q":
		break
	elif tokens[0] == "+":
		print add(int(tokens[1]), int(tokens[2]))
	elif tokens[0] == "-":
		print subtract(int(tokens[1]), int(tokens[2]))
	elif tokens[0] == "*":
		print multiply(int(tokens[1]), int(tokens[2]))
	elif tokens[0] == "/":
		print divide(int(tokens[1]), int(tokens[2]))
	elif tokens[0] == "**2":
		print square(int(tokens[1]))
	elif tokens[0] == "**3":
		print cube(int(tokens[1]))
	elif tokens[0] == "**":
		print power(int(tokens[1]), int(tokens[2]))
	elif tokens[0] == "%":
		print mod(int(tokens[1]), int(tokens[2]))