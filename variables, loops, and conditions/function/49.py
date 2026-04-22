# Write a Python program to check if a number is prime.

def check_prime(number):
    if number < 2:
        print("prime number")
    
    else:
        print("not a prime number")

a = int(input("enter any number"))

prime = check_prime(a)

print(prime)

