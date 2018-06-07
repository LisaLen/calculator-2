"""Math functions for calculator."""


def add(lst):
    """Return the sum of the two inputs."""

    return float(lst[0]) + float(lst[1])

def subtract(lst):
    """Return the second number subtracted from the first."""

    return float(lst[0]) - float(lst[1])



def multiply(lst):
    """Multiply the two inputs together."""

    return float(lst[0]) * float(lst[1])



def divide(lst):
    """Divide the first input by the second, returning a floating point."""

    return float(lst[0]) / float(lst[1])



def square(lst):
    """Return the square of the input."""

    # Needs only one argument

    return float(lst[0]) ** 2 


def cube(lst):
    """Return the cube of the input."""

    # Needs only one argument

    return float(lst[0]) ** 3

def power(lst):
    """Raise num1 to the power of num and return the value."""

    return float(lst[0]) ** float(lst[1])  # ** = exponent operator


def mod(lst):
    """Return the remainder of num / num2."""

    return float(lst[0]) % float(lst[1])

