# Write:

# register_student(name, course, fee)

# 👉 Call using keyword arguments in any order.

def register_student(name, course, fee):
    print(f"name = {name}, course = {course}, fee = {fee}")

a = input("what is your name")
b = input("which course you taken")
c = input("what is your fees")

register_student(name=a, course=b, fee=c)

