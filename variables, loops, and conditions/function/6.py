# Write a function that takes two numbers and returns the larger one.

def larg():
    a = int(input("enter your first number"))
    b = int(input("enter your second number"))


    if a > b:
        print("first number are larger",)
    
    elif b > a:
        print("second number are larger",)

    else:
        print("both are equal")

larg()