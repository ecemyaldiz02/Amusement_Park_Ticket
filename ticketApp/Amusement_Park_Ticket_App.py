
print("Welcome to the rollercoaster ! :)")

height = int(input("What is your height in cm ?"))
bill = 0
if height >=120:
    weight = int(input("What is your weight in kg ?"))
    if weight >=85:
        print("You can not ride the rollercoaster ! :)")
    else :
        print("You can ride the rollercoaster ! :)")
    age = int(input("What is your age?"))
    if age >= 18:
        bill = 15
        print("You must buy an adult ticket (15$)! :)")
    elif 12<=age<=18:
        bill = 11
        print("You must buy an young ticket (11$)! :)")
    elif age<12:
        bill = 10
        print("You must buy an child ticket (10$)! :)")
    photo = input("Do you want any photo ? (Y/N)")
    if photo == "Y":
        bill+=5
        print(f"Your bill is : {bill} $")
    else:
        print(f"Okey,your bill is : {bill} $")
else :
    print("You can not ride the rollercoaster ! :(")