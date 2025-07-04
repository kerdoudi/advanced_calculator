# calculator.py

def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    print("Welcome to the calculator")
    print("2 + 3 =", add(2, 3))
    print("5 - 2 =", subtract(5, 2))
    print("10 / 2 =", divide(10, 2))

if __name__ == "__main__":
    main()