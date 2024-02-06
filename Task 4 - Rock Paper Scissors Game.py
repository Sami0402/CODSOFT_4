rock='''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    '''

paper='''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    '''
scissors='''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
      '''
#user and computer scores
user_score=0
computer_score=0

import random
choice="yes"
while choice!="no":
    options=[rock,paper,scissors]
    user_choice=int(input("What do you choose ? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
    if user_choice>=3:
        print("You type an invalid number, you lose!")
        computer_score+=1
        print("You Lose\n")
    else:
        print("You chose:")
        print(options[user_choice])
        computer_choice=random.randint(0,2)
        print("Computer chose:")
        print(options[computer_choice])

        #Rock(0) Vs paper(1)=paper(1)
        #Rock(0) Vs scissors(2)=rock(0)
        #paper(1) Vs scissors(2)=scissors(2)
        #If both same the Tie

        #Rules
        if user_choice==computer_choice:
            user_score+=0
            computer_score+=0
            print("It's a draw\n")
        elif user_choice==0 and computer_choice==2:
            user_score+=1
            print("You Win!!!\n")
        elif user_choice==2 and computer_choice==0:
            computer_score+=1
            print("You Lose\n")
        elif user_choice>computer_choice:
            user_score+=1
            print("You Win!!!\n")
        elif user_choice<computer_choice:
            computer_score+=1
            print("You Lose\n")
    print(f"Your score = {user_score} Vs Computer's score = {computer_score}\n")

    #Ask the the user if they want to play another round
    choice=input("Do you want to play another round ?Type 'yes' or 'no' :")

