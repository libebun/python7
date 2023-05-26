# 1,2
age = 18
if age > 100:
    print("liar")
elif age > 18:
    print("Okay")
elif age < 0:
    print("You`re not born")
elif age < 18:
    print("Nope")
else:
    print("You are: " + str(age))
# 3
if age % 2 == 0:
    print("even")
else:
    print("odd")
# 4,5
name = "Katherine"
if 'a' in name:
    print("Not checking your name, " + name + ".")
elif 'v' in name.lower() and age % 2 == 0:
    print("You won a prize, " + name + ".")
else:
    print("You did not win a prize, " + name + ".")
