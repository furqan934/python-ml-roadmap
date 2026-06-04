# Function in The Python 
# Author: Satyarth Mishra
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b
def main():
    print("Welcome to the Simple Calculator!")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Choose an operation (+, -, *, /): ")
    
    if operation == '+':
        result = add(num1, num2)
        print(f"The result of {num1} + {num2} is: {result}")
    elif operation == '-':
        result = subtract(num1, num2)
        print(f"The result of {num1} - {num2} is: {result}")
    elif operation == '*':
        result = multiply(num1, num2)
        print(f"The result of {num1} * {num2} is: {result}")
    elif operation == '/':
        result = divide(num1, num2)
        print(f"The result of {num1} / {num2} is: {result}")
    else:
        print("Invalid operation. Please choose from +, -, *, /.")

if __name__ == "__main__":
    main()