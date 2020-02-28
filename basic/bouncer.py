# ask for age
age = input("How old are you?\n")

if age:
    if 18 <= int(age) < 21:
        # 18-21 wristband
        print("You can enter, but you need a wristband!")
    elif int(age) >= 21:
        # 21+ drink, normal entry
        print("You're good to enter and can drink!")
    else:
        # too young, sorry
        print("You can't come in, little one!")
else:
    print("Please enter an age!")
