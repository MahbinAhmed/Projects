#Rock, Paper, Scissor

import random

bot_choice_list=["Rock","Paper","Scissor"]
random_choice = random.choice(bot_choice_list)

a = 1
computer_point = 0
your_point = 0
print("-----Welcome to Rock paper scissor game-----")
while a<=10:
    random_choice = random.choice(bot_choice_list)
    input1=input("Press r for Rock, p for Paper, s for Scissor : ")
    if input1=="r":
        if random_choice=="Rock":
            print("Game tie")
            print(random_choice)
            your_point=your_point+0
            computer_point=computer_point+0
        elif random_choice=="Scissor":
            print("You won")
            print(random_choice)
            your_point=your_point+1
        elif random_choice=="Paper":
            print("You loose")
            print(random_choice)
            computer_point=computer_point+1
    elif input1=="p":
        if random_choice=="Paper":
            print("Game tie")
            print(random_choice)
            your_point=your_point+0
            computer_point=computer_point+0
        elif random_choice=="Rock":
            print("You won")
            print(random_choice)
            your_point=your_point+1
        elif random_choice=="Scissor":
            print("You loose")
            print(random_choice)
            computer_point=computer_point+1
    elif input1=="s":
        if random_choice=="Scissor":
            print("Game tie")
            print(random_choice)
            your_point=your_point+0
            computer_point=computer_point+0
        elif random_choice=="Paper":
            print("You won")
            print(random_choice)
            your_point=your_point+1
        elif random_choice=="Rock":
            print("You loose")
            print(random_choice)
            computer_point=computer_point+1
    else:
        print("Enter between r,p,s")
    a+=1

if computer_point<your_point:
    print("\n\nYou won the game")
elif computer_point==your_point:
    print("\n\nGame tied")
else:
    print("\n\nYou loose the game")

print(f"Your point is {your_point}")
print(f"Computer point is {computer_point}")