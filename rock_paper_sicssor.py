import random
while True:
    choices = ["Rock","Paper","Sicssor"]
    player = input("choose Rock ,Paper or Scissor: ")
    computer = random.choice(choices)
    if player == computer:
        print("This match is tie well played next time I will won")
    elif(
        (player =="Rock" and computer =="Sicssor")or\
        (player == "Sicssor"and computer =="Paper")or\
        (player =="Paper"and computer == "Rock")
    ):
        
        print(f"Ooo you win {player} beats {computer}")
        break
    else:
        print(f"You lost the game {computer} beats {player}")
      