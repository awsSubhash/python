# Write a function:

# student(name, age, marks)

# 👉 Call the function using keyword arguments and print details.

def student(name, age, marks):
    print(f"your name is {name}, your age is {age}, your marks is {marks}")

a = str(input("what is your name"))
b = int(input("what is your age"))
c = int(input("what is your marks"))


student(a, b, c)

