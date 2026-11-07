def apples_disteibutor(a,b):
    # a = int(input("Enter Number of apples: "))
    # b= int(input("Enter Number of students: "))

    if a % b == 0:
        
        print(f"Every student will get {a//b }")
    elif a %b != 0:
        extra = b - (a%b)
        print("Every student will not get the equal apples")
        print(f"for equal distubution of the appples {extra} apples needed ")

apples_disteibutor(203,5)


