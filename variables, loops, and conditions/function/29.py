# Create a function to display student result with default pass mark.

def result(science, math , english, hindi, passmark=300):
    total = science + math + english + hindi
    print("Total marks is", total)
    if total >= passmark:
        print("your are pass")
    
    else:
        print("sorry bro you are not pass")

a = int(input("what is science subject marks"))
b = int(input("what is math subject marks"))
c = int(input("what is english subject mark"))
d = int(input("what is hindi subject marks"))

result(a, b, c, d)