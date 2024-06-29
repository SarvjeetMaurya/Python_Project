import random

rock ='''   _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

paper ='''    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)'''

scissor ='''    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
your_choice = int(input("What do you want to choose: Rock for 0, Paper for 1 and Scissor for 2 \n"))
computer_choice = random.randint(0,2)

if your_choice == 0 and computer_choice== 0:
    print("You choose: Rock\n",rock)
    print("Computer choose:Rock \n",rock)
    print("The match Draw..")
elif your_choice ==0 and computer_choice==1:
      print("You choose: Rock\n",rock)
      print("Computer choose: Paper\n",paper)
      print("Sorry you loose the game....")
elif your_choice ==0 and computer_choice ==2:
      print("You choose: Rock\n",rock)
      print("Computer Choose: Scissor\n",scissor)
      print("Hurry, you won the game....")

elif your_choice == 1 and computer_choice== 1:
    print("You choose: Paper \n",paper)
    print("Computer choose: Paper \n",paper)
    print("The match Draw..")
elif your_choice == 1 and computer_choice==2:
      print("You choose: Paper\n",paper)
      print("Computer choose: Scissor\n",scissor)
      print("Sorry you loose the game....")
elif your_choice == 0 and computer_choice ==0:
      print("You choose: Paper\n",paper)
      print("Computer Choose: Rock\n",rock)
      print("Hurry, you won the game....")

elif your_choice == 2 and computer_choice== 2:
    print("You choose: Scissor \n",scissor)
    print("Computer choose: Scissor \n",scissor)
    print("The match Draw..")
elif your_choice ==2 and computer_choice==0 :
      print("You choose:Scissor \n",scissor)
      print("Computer choose: Rock\n",rock)
      print("Sorry you loose the game....")
elif your_choice == 2 and computer_choice ==1:
      print("You choose: Scissor\n",scissor)
      print("Computer Choose: Paper\n",paper)
      print("Hurry, you won the game....")
else:
     print(f"{your_choice}, is the invailed input..")