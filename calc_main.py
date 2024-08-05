# main.py

import calculator

def get_number(prompt):
    """Get a number from the user."""
    while True:
        try:
            number = float(input(prompt))
            return number
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operation():
    """Get an arithmetic operation from the user."""
    operations = {'+': calculator.add, '-': calculator.subtract, '*': calculator.multiply, '/': calculator.divide}
    while True:
        operation = input("Enter an operation (+, -, *, /): ")
        if operation in operations:
            return operations[operation]
        else:
            print("Invalid operation. Please enter one of +, -, *, /.")

def main():
    print("Simple Calculator")
    num1 = get_number("Enter the first number: ")
    num2 = get_number("Enter the second number: ")
    operation = get_operation()

    try:
        result = operation(num1, num2)
        print(f"The result is: {result}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
