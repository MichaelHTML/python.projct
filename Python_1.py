
from ast import If
from functools import partial
from pydoc import plain
from random import randint, random


print("rock.....")
print("paper.....")
print("scissors.....")


radomNumber = randint(0 , 2)


if radomNumber == 0 :
    computerMove = "rock"
elif radomNumber == 1:
    computerMove = "paper"
elif radomNumber == 2 :
    computerMove = "scissore"

player_1 = input("player_1 , make you move : ") 
player_2 = computerMove
print(f"player_2 , make you move : {computerMove} ")


if player_1 == player_2 :
    print("thats a tie.....")
elif player_1 == "rock" and player_2 == "paper" :
    print("player_2 win.....")
elif player_1 == "rock" and player_2 == "scissors" :
    print("player_1 win......")
elif player_1 == "paper" and player_2 == "rock" :
    print("player_1 win......")
elif player_1 == "paper" and player_2 == "scissors" :
    print("playre_2 win......")
elif player_1 == "scissors" and player_2 == "rock" :
    print("playe_2 win........")
elif player_1 == "scissors" and player_2 == "paper" :
    print("playe_1 win........")
else :
    print("something went wrong.......")





