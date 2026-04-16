# Find the largest of three numbers using conditional statements.

a = input("enter your science marks ")

b = input("enter your maths marks ")

c = input ("enter your english marks ")

a = int(a)
b = int(b)
c = int(c)

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

print ("largest number is ", largest)