# hello.py
# Date: 11 June 2025
# Author: John

print("Hello from Python!")

# Print a welcome message
print("Hello! Welcome to your first Python program.")

# Get user input
name = input("What is your name? ")

# Function to greet the user
def greet(user_name):
    print(f"Nice to meet you, {user_name}!")

greet(name)

# Simple math operation
a = 5
b = 3
sum = a + b
print(f"The sum of {a} and {b} is {sum}.")

# If-else example
if sum > 5:
    print("That's a pretty big number!")
else:
    print("That's a small number.")

# Loop example
print("Now let's count from 1 to 5:")
for i in range(1, 6):
    print(i)
