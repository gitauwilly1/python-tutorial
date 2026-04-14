# Simple Calculator

# This program prompts the user for two numbers and an arithmetic operator,
# performs the corresponding calculation, and displays the result.

# Step 1: Prompt the user for the first number and convert it to a float
# to allow decimal calculations.
num1 = float(input("Enter the first number: "))

# Step 2: Prompt the user for the operator.
operator = input("Enter an operator (+, -, *, /): ")

# Step 3: Prompt the user for the second number and convert it to a float.
num2 = float(input("Enter the second number: "))

# Step 4: Initialize a variable to store the calculation result.
result = 0

# Step 5: Use conditional statements to determine which operation to perform.
if operator == '+':
    result = num1 + num2  # Addition
elif operator == '-':
    result = num1 - num2  # Subtraction
elif operator == '*':
    result = num1 * num2  # Multiplication
elif operator == '/':
    # Division requires a safety check to avoid dividing by zero.
    if num2 == 0:
        print("Error: Division by zero is not allowed.")
    else:
        result = num1 / num2  # Division
else:
    # Handle cases where the user inputs an unsupported operator.
    print("Error: Invalid operator. Please use +, -, *, or /.")

# Step 6: Display the final result in a formatted string.
print(f"\nResult: {num1} {operator} {num2} = {result}")