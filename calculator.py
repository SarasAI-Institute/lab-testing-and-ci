import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def power(a, b):
    return a ** b

def square_root(a):
    return math.sqrt(a)

def calculate_stats(numbers):
    return sum(numbers) / len(numbers)

if __name__ == "__main__":
    print("2 + 2 =", add(2, 2))
    print("10 / 0 =", divide(10, 0)) # This will crash
