from ast import Num
import random
guess = int(input("Enter the number : "))
num = random.randint(1,101)
guesses = 1
while(guess != num):
    if(guess<num):
        print("Enter the greater number ")      
    else:
        print("Enter the smaller number ")
    guess = int(input("Enter the number : "))
    guesses += 1

print(f"You have guessed the number in {guesses} attempts!! ")
