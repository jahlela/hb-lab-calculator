from functools import reduce

def add(int_list):
    """ Returns the sum of the inputs"""
    total = reduce((lambda x, y: x+y), int_list)
    return total

def subtract(int_list):
	"""Returns the result of subtracting the second number from the first"""
	total = reduce((lambda x, y: x-y), int_list)
	return total

def multiply(int_list):
	"""Returns the product of the inputs"""
	total = reduce((lambda x, y: x*y), int_list)
	return total

def divide(int_list):	
	"""Divides the first input by the second, returning a floating point number"""
	total = reduce((lambda x, y: x/y), int_list)
	return total

def square(int_list):
	"""Returns the square of the input"""
	total =  int_list**2
	return total

def cube(int_list):
	"""Returns the cube of the input"""
	total =  int_list**3
	return total

def power(int_list):
	"""Returns the result of raising the first input to the power of the second input"""
	total = reduce((lambda x, y: x**y), int_list)
	return total

def mod(int_list):
	"""Returns the remainder when the first input is divided by the second input"""
	total = reduce((lambda x, y: x%y), int_list)
	return total