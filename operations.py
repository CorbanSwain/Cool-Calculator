#!/bin/python3
# operations.py

sym_dict = {}


# ADDITION Operation Entry #################################
# Desired Functionality: (+ a b) = a + b

def add(a, b):
    return a + b

# name of function -v    v------ Name of function author
sym_dict['+'] = ('add', 'Corban S.')
############################################################



# SUBTRACTION Operation Entry ##############################
# Desired Functionality: (- a b) = a-b

def subtract(a, b):
	return a-b

sym_dict['-'] = ('subtract', 'Nic & iguptasn')
############################################################



# DIVISION Operation Entry #################################
# Desired Functionality: (/ a b) = ???

def divide(a, b):
    return 0


sym_dict['/'] = ()
############################################################



# MULTIPLICATION Operation Entry ###########################
# Desired Functionality: (* a b) = ???

def multiply(a, b):
    return 0


sym_dict['*'] = ()
############################################################



# EXPONENTIATION Operation Entry ###########################
# Desired Functionality: (^ a b) = a ** b
# Hint: exponentiation in python is performed with the `**` symbol

def power(a, b):
    return a**b
    # return 0


sym_dict['^'] = ('power','does it work? - YoungGyu')
############################################################



# AND Operation Entry ###########################
# Desired Functionality: (& a b) = a and b

def _and(a, b):
    return a and b


sym_dict['&'] = ('_and', 'Corban Swain')
############################################################
