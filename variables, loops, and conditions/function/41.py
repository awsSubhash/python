# 11. Calculator with Named Inputs

 # Create calculate(num1, num2, operation)
# Use keywords to specify operation like "add" or "multiply".


def calculate(num1, num2, operation):
    if operation == "add":
        return num1 + num2
    if operation == "multiply":
        return num1 * num2
    else:
        return "invalid operation"

a = int(input("enter any number"))

c = int(input("enter second any number"))


op = input("Enter operation (add/multiply): ")

calculate(a, op, c)