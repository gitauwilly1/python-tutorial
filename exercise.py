# EXERCISE 1: Name Welcome Program

# This program prompts the user for their name and prints a welcome message.

# Prompt the user to enter their name and store the input as a string
name = input("Enter your name: ")

# Print a personalized greeting using string concatenation
print("Hello " + name)


# EXERCISE 2: Gross Pay Calculator

# This program calculates gross pay based on hours worked and hourly rate.

# Prompt the user for hours worked and convert input to float
hours = float(input("Enter Hours: "))

# Prompt the user for rate per hour and convert input to float
rate = float(input("Enter Rate: "))

# Calculate gross pay by multiplying hours by rate
pay = hours * rate

# Print the calculated pay
print("Pay:", pay)


# EXERCISE 3: Expression Values and Types

# Given assignments:
width = 17
height = 12.0

# Let's evaluate each expression and check value + type:

# Expression 1: width//2
# is floor division → returns the largest integer ≤ the result
expr1 = width // 2
print(f"width//2 = {expr1}, type: {type(expr1).__name__}")
# Value: 8, Type: int

# Expression 2: width/2.0
# / is true division → always returns a float
expr2 = width / 2.0
print(f"width/2.0 = {expr2}, type: {type(expr2).__name__}")
# Value: 8.5, Type: float

# Expression 3: height/3
# height is a float (12.0), so result is float
expr3 = height / 3
print(f"height/3 = {expr3}, type: {type(expr3).__name__}")
# Value: 4.0, Type: float

# Expression 4: 1 + 2 * 5
# Order of operations: multiplication before addition → 2*5=10, then 1+10=11
expr4 = 1 + 2 * 5
print(f"1 + 2 * 5 = {expr4}, type: {type(expr4).__name__}")
# Value: 11, Type: int


# EXERCISE 4: Temperature Converter

# This program converts a Celsius temperature to Fahrenheit.
# Formula: F = (C × 9/5) + 32

# Prompt the user for temperature in Celsius and convert to float
celsius = float(input("Enter temperature in Celsius: "))

# Apply the conversion formula
fahrenheit = (celsius * 9/5) + 32

# Print the converted temperature
print(f"{celsius}°C is equal to {fahrenheit}°F")

