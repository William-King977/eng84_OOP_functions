# What are functions?
# Why functions?

# Syntax def function_name():
# def tells the interpreter that the function is being created

# Creating a greeting function
# def greeting():
#     print("Welcome on board.")
#
# # The function must be called to display the output
# greeting()

# Function to take an argument
# def greeting(name):
#     print("Welcome on board " + name + ".")
# greeting("King")

# Two arguments. Outputs the addition of two numbers.
# def add(num1, num2):
#     print(num1 + num2)
# add(4, 10)

# Using a return statement
# def sum_return(num1, num2):
#     return num1 + num2
# print(sum_return(2, 4))

# Create a calculator to add, subtract, divide, multiply
# display appropriate messages with the computation values as to what the outcome is from each function
# create a greeting function by taking user input as the user name and display it with the greeting message

# Addition
def add(num1, num2):
    return num1 + num2

# Subtraction
def subtract(num1, num2):
    return num1 - num2

# Division
def divide(num1, num2):
    return num1 / num2

# Multiplication
def multiply(num1, num2):
    return num1 * num2

# Enter two numbers then calculate them
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print(f"{num1} + {num2} = {add(num1, num2)}")
print(f"{num1} - {num2} = {subtract(num1, num2)}")
print(f"{num1} / {num2} = {divide(num1, num2)}")
print(f"{num1} x {num2} = {multiply(num1, num2)}")

# Greeting function
def greeting(name):
    print(f"Hello {name}! Welcome!")

my_name = input("Enter your name: ")
greeting(my_name)






