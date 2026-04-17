# Create a function for simple interest with default rate.


def simple_interest(principal, time, rate=5.0):
    return (principal * time * rate) / 100

a = int(input("What is your principal amount? "))
b = int(input("What is your time? "))

result = simple_interest(a, b)
print("Simple Interest is:", result)