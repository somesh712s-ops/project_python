import random 
while True:
    choices = ["snake","water","gun"]
    playerchoice = str(input("Enter your choice: "))
    computer = random.choice(choices)
    if playerchoice == computer:
        print("This match is tie:")
    elif(
        (playerchoice == "gun" and computer =="snake")or\
        (playerchoice == "water" and computer =="gun")or\
        playerchoice == "snake" and computer =="water"
    ):
        print(f"Ooo Nice your {playerchoice} beats {computer} ")
        break
    else:
        print(f"Ooo No {computer} beats {playerchoice}")
    