#dice roller
import random

def dice():
    return random.randint(1,6)

while True:
    print(dice())
    if input("Do you want to roll again? (yes/no): ").lower() != "yes":
        break