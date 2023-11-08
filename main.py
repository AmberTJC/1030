import calculator

first_input = input ("Please enter the first number ")
second_input = input ("Please enter the second number ")
operation = input ("Would you like to add/subtract/multiply/divide: ")

first_number = float (first_input)
second_number = float (second_input)

if operation == "add":
    calculator.addition (first_number, second_number)
elif operation == "subtract":
    calculator.subtraction (first_number, second_number)
elif operation == "multiply":
    calculator.multiplication(first_number, second_number)
elif operation == "divide":
    calculator.division (first_number, second_number)
else:
    print ("Sorry I do not understand your request")