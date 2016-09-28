def add(num1, num2):
    """ Returns the sum of the inputs"""
    
    return num1 + num2

def subtract(num1, num2):
	"""Returns the result of subtracting the second number from the first"""
	return num1 - num2

def multiply(num1, num2):
	"""Returns the product of the inputs"""
	return num1 * num2

def divide(num1, num2):	
	"""Divides the first input by the second, returning a floating point number"""
	return float(num1) / num2

def square(num1):
	"""Returns the square of the input"""
	return num1 ** 2
	

def cube(num1):
	"""Returns the cube of the input"""
	return num1 ** 3

def power(num1, num2):
	"""Returns the result of raising the first input to the power of the second input"""
	return num1 ** num2

def mod(num1, num2):
	"""Returns the remainder when the first input is divided by the second input"""
	return num1 % num2
	

print add(4,5)
print subtract(56,9)
print multiply(2,70)
print divide(5,4)
print square(5)
print cube(5)
print power(5,4)
print mod(5,1)