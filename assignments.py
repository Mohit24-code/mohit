#TASK 1
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform operations
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

# Handle division by zero
if num2 != 0:
    division = num1 / num2
else:
    division = "Undefined (division by zero)"

# Display results
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")
#/////////////////////////////////////////////////////////////////////////////////////////////////////
#TASK 2
# Take user's first name and last name as input
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

# Concatenate first name and last name
full_name = first_name + " " + last_name

# Print personalized greeting
print(f"Hello, {full_name}! Welcome to the python program")