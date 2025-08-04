# This ask the user to input the first number
num1 = float(input("Enter the first number: "))

# This ask the user to input the second number
num2 = float(input("Enter the second number: "))

# This ask the user to choose an operation: +, -, *, or /
operation = input("Enter the operation (+, -, *, /): ")

# This perform the operation based on the user's input
if operation == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")

elif operation == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")

elif operation == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")

elif operation == "/":
    # Check to avoid dividing by zero
    if num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Division by zero is not allowed.")

else:
    # This message pop up when1 the user enters an invalid operation
    print("Invalid operation. Please enter +, -, *, or /.")
