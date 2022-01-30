"""Winning Rules as follows :

Rock vs paper-> paper wins
Rock vs scissor-> Rock wins
paper vs scissor-> scissor wins."""

#from random import random
import random as rand

player1=input("Enter name of player 1: ")
score1=0
score2=0

'''
rock=1
paper=2
scissor=3
''' 

game_count=int(input("How many times do you want to play? "))

print("----------------------------")

for i in range(game_count):
    print("choose any number:\nRock=1\nPaper=2\nScissor=3\n")
    a=int(input("Enter "+player1+" object number: "))
    if(a==1):
        print("You selected ROCK")
    if(a==2):
        print("You selected PAPER")
    if(a==3):
        print("You selected SCISSORS")
    b=rand.randint(1,3)
    if(b==1):
        print("Computer selected ROCK")
    if(b==2):
        print("Computer selected PAPER")
    if(b==3):
        print("Computer selected SCISSORS")

    print("\n")
    
    if (a==1 and b==2):
        score2=score2+1
        print("Computer wins\nScore of computer= +1\n")
    
    elif (a==1 and b==3):
        score1=score1+1
        print(player1+" wins\nScore of "+player1+"= +1\n")
    
    elif (a==2 and b==3):
        score2=score2+1
        print("Computer wins\nScore of computer= +1\n")
    
    elif (a==2 and b==1):
        score1=score1+1
        print(player1+" wins\nScore of "+player1+"= +1\n")
    
    elif (a==3 and b==2):
        score1=score1+1
        print(player1+" wins\nScore of "+player1+"= +1\n")
    
    elif (a==3 and b==1):
        score2=score2+1
        print("Computer wins\nScore of computer= +1\n")
    
    elif(a==b):
        print("Draw, no score added")
    
    else:
        print("Please select numbers from 1, 2, 3...\n")

    print("Your total score= "+str(score1)+"\nComputer total score: "+str(score2))
    print(str(game_count-(i+1))+" trials left!!!")
    
    print("----------------------------")

print("Game ended!!\n")
print("Final score as follows-\n")
print("Score of "+player1+" is- "+str(score1))
print("Score of computer is- "+str(score2))

if(score1>score2):
    print("Hurray!!! You won the match")
elif(score1<score2):
    print("Sorry!!! You lost the match")
else:
    print("It's a DRAW match")