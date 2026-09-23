import math

first_number = int(input("Enter first number: "))
operation = input("Enter operation (+, -, *, /: ")
second_number = int(input("Enter second number: "))

if operation == "+":
    result = first_number + second_number
elif operation == "-":
    result = first_number - second_number
elif operation == "*":
    result = first_number * second_number
elif operation == "/":
    if second_number !=0:
        result = first_number / second_number
    else:
        result = "Cannot divide by zero"
else:
    result = "Invalid operation"

result = ("Result:", result)