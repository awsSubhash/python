# Create a function to validate password length (default min length = 8).


def checkpass(password, m_len=8):
    return len(password) >= m_len

password = input("what is your password")

if checkpass(password):
    print("your password is safe")

else:
    print("you password is not safe")


