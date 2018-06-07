"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def calculator(request):
    lst = request.split()
    
    if lst[0] == '+': 
        return add(lst[1:])

    elif lst[0] == '-':
        return subtract(lst[1:])

    elif lst[0] == '*':
        return multiply(lst[1:])

    elif lst[0] == '/':
        return divide(lst[1:])

    elif lst [0] == 'square':
        return square(lst[1])

    elif lst [0] == 'cube':
        return cube(lst[1])

    elif lst[0] == 'pow':
        return power(lst[1:])

    elif lst[0] == 'mod':
        return mod(lst[1:])



while True:
    command = input('>')
    if command == 'q' or command == 'quit': break
    print(calculator(command))
