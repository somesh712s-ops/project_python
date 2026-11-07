a = int(input("Enter your age or the year of birth: "))

if  150 <= a <=1800:
    print("put the correct and logical input")
    exit()

if a <150:
    age = True
    print("Thanks for your age")

elif a > 1800 :
    age = False
    year = True

    print("Thanks for your year of birth")
if year < 2026:
    print("say something logical you are not born yet")
    exit()

if age > 100:
    print("Nice bro you already in 10 % poplution of earth ")
    
print("1.when you turn 100")
print("2.want to know time to age:")

user = int(input("Enter your choice: "))
if user == 1:
    if age:
        c = 100 - a
        d = 2026 + c
        print(f"In year of {d} you will turn the age of 100")
    elif year:
        print(f"In year of {a+100} you will turn the age of 100")

elif user == 2:
    e = int(input("What expected age you want to calculate: "))
    if age:
        f = e - a 
        g = 2026 + f
        print(f"In year of {g} you will turn age of {e}")
    elif year:
        print(f"In year of {a+e} you will turn age of {e}") 

