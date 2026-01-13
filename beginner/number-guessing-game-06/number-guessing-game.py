# number guessing game
import random
import string

def nums():
    num = random.randint(1, 100)
    return num

num = nums()

while True:
    guess = int(input("Enter a number between 1 and 100: "))
    if guess == num:
        print("Congratulations! You guessed the number.")
        break
    elif guess > num:
        print("Too high! Try again.")
    else:
        print("Too low! Try again.")