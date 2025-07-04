# calculator.py

import math

def sqrt(a):
    if a < 0:
        return "Error: negative input"
    return math.sqrt(a)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    print("Welcome to the calculator")
    print("2 + 3 =", add(2, 3))
    print("5 - 2 =", subtract(5, 2))
    print("sqrt(16) =", sqrt(16))

if __name__ == "__main__":
    main()