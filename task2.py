# 6
name = input("Enter your name: ")
age = int(input("Enter your age: "))
sex = input("Enter your sex (m/f): ")

if sex not in ["m", "f"] or age < 0 or age > 100 or not name.isalpha():
    print("Invalid data.")
elif age < 15:
    print("We recommend tennis.")
elif 'c' in name.lower() or 't' in name.lower():
    print("We do not recommend sport.")
elif sex == "m" and age > 15:
    print("We recommend football.")
elif sex == "f" and age > 15:
    print("We recommend basketball.")
