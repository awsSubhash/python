# Write a function to calculate salary with default bonus.

def bonus(salary, bonus=5000):
    return salary + bonus

a = int(input("what is your salary"))

salary_bonus = bonus(a)

print("your total salary including bonus is ", salary_bonus)