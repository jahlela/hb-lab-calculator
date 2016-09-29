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




def intifier(tokens):
	""" Returns a list of an operator and integers.

	Takes a list of strings and converts all but the first to integers.	  """

	#starts off list with operator
	calculator_list = [tokens[0]]

	#change each stringy number to an integer and add it to calculator_list
	for each in tokens[1:]:
		each = int(each)
		calculator_list.append(each)

	return calculator_list


#create a while loop
while True:
	#Prompt the user for an arithmetic function and save input 
	input = raw_input("Enter a statement > ")
	tokens_input = input.split(" ")
	tokens = intifier(tokens_input)

	#Checks operator and calls arithmetic function accordingly
	if tokens[0] == "q" or tokens[0] == "quit":
		break
	elif tokens[0] == "+":
		print add(tokens[1], tokens[2])
	elif tokens[0] == "-":
		print subtract(tokens[1], tokens[2])
	elif tokens[0] == "*":
		print multiply(tokens[1], tokens[2])
	elif tokens[0] == "/":
		print divide(tokens[1], tokens[2])
	elif tokens[0] == "square":
		print square(tokens[1])
	elif tokens[0] == "cube":
		print cube(tokens[1])
	elif tokens[0] == "power":
		print power(tokens[1], tokens[2])
	elif tokens[0] == "mod":
		print mod(tokens[1], tokens[2])


