# arithmetic.py

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Нельзя делить на ноль")
    return x / y

def modulus(x, y):
    return x % y
