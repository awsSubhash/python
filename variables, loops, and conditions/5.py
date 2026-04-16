# Write a program to count how many variables are integers in a list.

a = input("Enter values: ").split()

count = sum(x.lstrip("-").isdigit() for x in a)

print(count)