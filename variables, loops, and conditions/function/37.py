# Function book(title, author, price) and print formatted output.

def book(title, author, price):
    print(f"Booking Title: {title}")
    print(f"Author name is: {author}" )
    print(f"Total price: {price}")

a = input("Booking name")
b = input("what is your name")
c = int(input("what is total price"))

book(a, b, c)