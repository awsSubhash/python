# 12. Movie Ticket Booking

# Function movie(name, seats, timing)
# Call using keyword arguments in different order.

def movie(name, seats, timing):
    print(f"you name {name}")
    print(f"your seats {seats}")
    print(f"your movie timing {timing}")

a = input("what is your name")

b = int(input("what is your seats"))

c = input("what is your movie time")

movie(timing=c, name=a, seats=b)

