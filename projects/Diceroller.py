import random
from sys import exit


def dice_roller():

    ans = input("How many sides do you want for the dice? ")

    print("How many times do you want to roll?", end=' ')
    imp = input()

    n = 0

    while int(imp) > n:

        print("Rolling the dice: ", random.randint(1, int(ans)))
        n += 1
        
    print("Do you want to go again? (y or n) ", end=' ')
    imp2 = input()

    if imp2 == "y":
        dice_roller()
    else:
        print("Exiting program...")
        exit(0)

dice_roller()