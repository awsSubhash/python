# Create a function for discount calculation with default discount = 10%.

def discount(price, discount=10):
    return price * discount /100

a = int(input("what is the total price"))

afterdiscount = discount(a)
print("The discount is ", afterdiscount)

# sum = afterdiscount - a
# print(sum)