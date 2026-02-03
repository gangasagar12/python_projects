"""
condition which is exits in the rock paper scissor game
 case 1: user enter the input from the self choice

 case 2: computer choice is an input radomly generated from the system
 case 3: result is decided on the basic of the system

#   case of the result
 1: in case rock
 cock vs paper : paper wins
 cock vs cock : match tie
 cock vs scissor: rock wins

 2: in case paper
 paper vs paper=match tie
 paper vs scissor= scissor wins
 paper vs rock=  paper wins

  3 : in case scissor
  scissor vs scissor :  match tie
  scissor vs paper : scissor wins
  scissor vs rock : rock wins
"""
import random

item_list=["rock","paper","scissor"]
user_choice=input("enter your choice( rock,paper,scissor): ")
computer_choice=random.choice(item_list)

print(f"user choice {user_choice}, computer choice is {computer_choice}")

if user_choice==computer_choice:
    print("both choice are same so , match tie")

elif user_choice=="rock":
    if computer_choice=="paper":
        print("computer wins")
    else:
       print("rock smashes scissor = you wins")
elif user_choice=="paper":
    if computer_choice=="scissor":
        print("computer wins")
    else:
        print("paper covers rock = you wins")
elif user_choice=="scissor":
    if computer_choice=="rock":
        print("computer wins")
    else:
        print("scissor cuts paper = you wins")