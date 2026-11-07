import random 
choices = (1,100)
computer = random.choice(choices)
count1 = 0
count2 = 0
while True:

    
    player1 = int(input("Gusse a No: "))
    count1 += 1
    player2 = int(input("Gusse a No: "))
    count2 += 1
    

    if computer == player1 or computer == player2:
        if computer == player1:
            winner = "player1"
        else:
            winner = "player2"
        class count:
            def __init__(self, count1, count2):
                self.count1 = count1
                self.count2 = count2

                self.count1 if winner == "player1" else self.count2
            

        print(f"Nice {winner} got the No . In {count1 if winner == 'player1' else count2} tries")
        exit()
        

    if computer > player1 and computer > player2:
        print("Ooo both gussed no is smaller")

    elif computer < player1 and computer < player2:
       print("Ooo both gussed no is higher")

    elif computer < player2 and computer > player1:
        print("Ooo player1 gussed no is smaller\nplayer2 gussed no is higher")

    elif computer > player2 and computer < player1:
        print("Ooo player2 gussed no is smaller\nplayer1 gussed no is higher")

            


    