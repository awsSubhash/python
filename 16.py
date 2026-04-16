# Check if a number is prime using loops and conditions.

for i in range(2, 50):
    is_prime = True

    for j in range(2, i):
        if i % j == 0:
            is_prime = False
            break

    if is_prime:
        print(i, "is a prime number")
    else:
        print(i, "is not a prime number")