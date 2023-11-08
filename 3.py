# Simple Calculator
print("Welcome to simple calculator.")
print("I will add/subtract/multiple/divide any two numbers you provide.")
first_input = input("Enter in first number: ")
second_input = input("Enter in second number: ")
operation = input("Would you like to add/subtract/multiple/divide: ")

# explicitly convert string type to float type
first_number = float(first_input)
second_number = float(second_input)

# function to add two numbers
def addition(first_number, second_number):
    result = first_number + second_number
    print (f"Result: {result}")

#function to subtract two numbers
def subtraction (first_number, second_number):
    result = first_number - second_number
    print (f"Result: {result}")

#function to multiply two numbers
def multiplication (first_number, second_number):
    result = first_number - second_number
    print(f"Result: {result}")

#function to divide two numbers
def division(first_number, second_number):
    result = first_number / second_number
    print (f"Result: {result}")

if operation == "add":
    addition(first_number, second_number)
elif operation == "subtract":
    subtraction(first_number, second_number)
elif operation == "multiply":
    multiplication (first_number, second_number)
elif operation == "divide":
    division (first_number, second_number)
else:
    print("Sorry, I do not understand your request.")
