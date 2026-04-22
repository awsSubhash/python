# Bank Account Creation

# Function create_account(name, balance=0, account_type="Savings")

def create_account(name, balance=0, account_type="savings"):
    print(f"your account name = {name}")
    print(f"your balance = {balance}")
    print(f"you account type = {account_type}")


a = input("what is your name")

create_account(a)