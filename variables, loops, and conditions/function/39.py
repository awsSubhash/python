# Online Shopping Cart

#Function:

#def cart(item, price, quantity=1)

# Call using keyword arguments and vary quantity.


def cart(item, price, quantity=1):
    print(f"item name {item}")
    print(f"what is the price {price}")
    print(f"Total quantity = {quantity}")


a = input("enter the item name")
b = int(input("what is price"))

cart(a, b, quantity=2)

