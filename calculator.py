"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def calculator(request):
    lst = request.split()
    num1 = float(lst[1])
    try:
        num2 = float(lst[2])
    except: num2 = None 

    if lst[0] == '+': 
        return add(num1, num2)

    elif lst[0] == '-':
        return subtract(num1, num2)

    elif lst[0] == '*':
        return multiply(num1, num2)

    elif lst[0] == '/':
        return divide(num1, num2)

    elif lst [0] == 'square':
        return square(num1)

    elif lst [0] == 'cube':
        return cube(num1)

    elif lst[0] == 'pow':
        return power(num1, num2)

    elif lst[0] == 'mod':
        return mod(num1, num2)



while True:
    command = input('>')
    if command == 'q' or command == 'quit': break
    print(calculator(command))
