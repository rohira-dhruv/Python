import random
from art import rock,paper,scissors
print("Welcome to the game of Rock Paper Scissors")
user_choice=int(input("Enter 0 for Rock, 1 for Paper and 2 for Scissors\n"))
options=[rock,paper,scissors]
if user_choice >=0 and user_choice<= 2:
  print("You chose:\n"+options[user_choice])
  comp_choice=random.randint(0,2)
  print("the Computer Chose: \n")
  print(options[comp_choice])
  if comp_choice-user_choice==1 or comp_choice-user_choice==-2:
    print("You lose")
  elif comp_choice==user_choice:
    print("It is a tie")
  else:
    print("You win")
else:
  print("Please enter the correct option") 