# calculator.py

def multiply(a, b):
    return a * b

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def main():
    print("Welcome to the calculator")
    print("2 + 3 =", add(2, 3))
    print("5 - 2 =", subtract(5, 2))
    print("3 * 4 =", multiply(3, 4))

if __name__ == "__main__":
    main()