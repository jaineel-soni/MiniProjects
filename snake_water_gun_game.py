import random
from re import L
print("Lets play snake,water and gun game ")
rules = '''
--> snake can win against water
--> water can win against gun
--> gun can win against snake
'''
l = ["snake", "water", "gun"]
print(rules)
youWon = 0
opponentWon = 0
a = int(input("press 1 to continue playing and press 5 to quit the game "))
while(a != 5):
    you = input("Choose snake, water or gun!!")
    opponent = random.choice(l)
    if(you == opponent):
       print("Its a tie !!")
    elif(you == "snake" and opponent == "water"):
       print("You won!!")
       youWon += 1
    elif(you == "water" and opponent == "gun"):
       print("you won!!")
       youWon += 1
    elif(you == "gun" and opponent == "snake"):
       print("you won!!")
       youWon += 1
    else:
       print("you lose")
       opponentWon += 1
    a = int(input("press 1 to continue playing and press 5 to quit the game "))

# print(f"you choose {you}")
# print(f"opponent choose {opponent}")
print(f"You won {youWon} games and opponent won {opponentWon} games !!")
