# Write a function to calculate power with default exponent = 2

def power(base, exponent=2):
    return base ** exponent
    
result = int(input("enter any number"))

print(power(result))

