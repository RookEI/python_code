import random

#This is the list of play options
t = ["Rock", "Paper", "Scissor"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("Rock", "Paper", "Scissor")
    if player == computer:
        print("Tie!")
elif player == "Rock":