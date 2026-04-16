# Given marks, print grade (A/B/C/D/F) using conditions.

science = int(input("science subject marks"))

math = int(input("math subject marks"))

english = int(input("english subject marks"))

all_marks = science + math + english

if all_marks >= 90:
    print("your grade is A")

elif all_marks >= 70:
    print("your grade is B")

elif all_marks >= 60:
    print("your grade c")

elif all_marks >= 50:
    print("your grade is D")

else:
    print("your grade is E")