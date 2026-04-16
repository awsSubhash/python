# Write a function that takes three numbers and returns their average.


def aver():
    a = int(input("enter your maths sub marks"))
    b = int(input("enter your english sub marks"))
    c = int(input("enter your hindi sub marks"))

    average = a + b + c / 3
    print("The average is =", average)

aver()