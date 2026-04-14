# Square Root Calculator

# This program calculates and prints the square root of a given number
# using Python's built-in math library.

# Step 1: Import the math module, which contains mathematical functions
# like sqrt(), pow(), floor(), etc.
import math

# Step 2: Prompt the user for a number and convert the input to a float.
# Note: math.sqrt() only works with non-negative numbers.
number = float(input("Enter a positive number to find its square root: "))

# Step 3: Calculate the square root using math.sqrt().
# This function returns a float representing the square root of the input.
square_root = math.sqrt(number)

# Step 4: Print the result in a clear, formatted string.
print(f"The square root of {number} is {square_root}")