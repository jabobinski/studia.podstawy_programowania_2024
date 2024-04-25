import random

def guess_number():
    target_number = random.randint(1, 9)
    while True:
        guess = int(input("Guess a number between 1 and 9:"))
        if guess == target_number:
            print("Good!")
            break
        else:
            print("Incorrect. Try again.")

guess_number()