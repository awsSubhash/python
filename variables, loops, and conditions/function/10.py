# add(a, b) Call it in different ways: 
# using positional arguments using keyword arguments in reverse order

def add(a, b):
    result = a + b
    print(f"a = {a}, b = {b}, sum = {result}")

num = int(input("enter any number"))
num1 = int(input("enter any number"))

add(num, num1)