# display welcome msg to the user

from random import randint
from art import  logo

EASY_ATTEMPT = 5
HARD_ATTEMPT = 10

#function to ask the difficulties

def difficuly():
    level = input("Choose the difficulty level: Type 'Easy' or 'Hard' ").lower()
    if level == 'easy':
        print(f"You have {EASY_ATTEMPT} attempts. ")
        turns = EASY_ATTEMPT
    elif level=='hard':
        print(f"You have {HARD_ATTEMPT} attempts. ")
        turns = HARD_ATTEMPT
    else :
        print("Invalid Input !")
        return 0

#function to check user guess number with computer generated number

def check(answer , guess):
    if guess>answer:
        print(f"{answer} is too high compared to guess number.")
    elif answer>guess:
        print(f"{answer} is too low compared to guess number.")
    else:
        print(f"You got it ! the answer was {answer} .")

print(logo)

print("Welcome to Guessing Game")
print("Think a number between 1 to 100! ")


#select the number
answer = randint(1,100)

#store the guess number

guess = int(input("What is your guess: "))







