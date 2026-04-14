# Random Number Generator

# This program generates and prints a random integer between 1 and 100.

# Step 1: Import the built-in random module, which provides functions
# for generating random numbers.
import random

# Step 2: Use randint() to generate a random integer.
# The function takes two arguments: the lower bound (1) and upper bound (100).
# Both bounds are inclusive.
random_number = random.randint(1, 100)

# Step 3: Print the generated number to the console.
print(f"Random number between 1 and 100: {random_number}")