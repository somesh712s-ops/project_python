questions = [
["1.What is the capital of India?","Mumbai","New Delhi","kolkata","Chennai",2],
["2.Which planet is known as the Red planet?","Venus","jupiter","Mars","Saturn",3],
["3.What is 15 x 8","100","110","120","125",3],
["4.Which gas is most abundant in Earth's","oxygen","Nitrogen","Carbon Dioxide","Hydrogen",2],
["5.What s chemical symbol for gold","Ag","Gd","Au","Go",3],
["6.Who wrote the Indian national anthem","Mahatma Gandhi","Radindranath Tagore","Sarojini naidu","Bk chattpadhyay",2],
["7.What is value of sqare root of 144","10","11","13","12",4],
["8.Which organ pumps blood throghout the human","Lungs","Brain","Kidney","Heart",4],
["9.Which of the Following is a programming","python","HTML","HTTP","URL",1],
["10.Water boils at what temperature at normal atm pressure","50 C","100C","90C","95C",2]
]

prize = [ 1000,2000,4000,6000,7000,9000,10000,11000,13000,20000]

i = 0
sum = 0

for question in questions:
    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")

    a =int(input("Enter your response: .1 for a,2 for b,3 for c,4 for d\n"))
    if(question[5]==a):
        print(f"Shai jabab apke jeete hai {prize[i]}")
        sum += prize[i]
        i += 1
    else:
        print(f"Galat jabab! shai jabab hai {question[5]}")
        print(f"koi nhai apka total prize hai {sum}")
        break

    
