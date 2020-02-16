from sys import exit


def start():

    print("""Welcome to the kungla_game.""")
    print("You walk into the kungla house, and are already greeted with choices.")
    print("Do you choose to go left or right?")

    choice1 = input("> ")

    if "left" in choice1:
        left_choice()
    elif "right" in choice1:
        right_choice()
    else:
        print("damn man, can you not read? choose left or right")
        start()

def GG(reason):

    print(reason, "GG.")
    exit(0)

def left_choice():

    print("You are now in the tv room.")
    print("There's a TV in here. also a dangerous caged Python")
    print("Do you wish to go forward or stay and watch tv?")

    choice2 = input("> ")

    if choice2 == "watch tv":
        GG("A mighty Python sneaked behind you and strangled you to death.")
    elif choice2 == "go forward":
        fire_place_room()
    else:
        print("""You have to type "go forward" or "watch tv" """)
        left_choice()

def fire_place_room():

    print("You have reached the fireplace room.")
    print("Pretty much a dead end, except for one last room here.")
    print("Do you wish to go back, or go forward?")

    choice3 = input("> ")

    if choice3 == "go back" or "back":
        start()
    elif choice3 == "go forward" or "forward":
        print("You have reached the sauna room.")
        GG("You take a shower and return back to start.")
    else:
        print("Try typing a little differently, perhaps")
        fire_place_room()

def right_choice():

    print("You have reached the kitchen.")
    print("Do you wish to stay, eat and end the game,")
    print("or continue with adventures upstairs?")

    choice = input("> ")
    if choice == "up" or choice == "go up" or choice == "go upstairs" or choice == "go next":
        upstairs_room()
    elif choice == "stay" or choice == "eat" or choice == "end":
        GG("You decide to stay and eat.")
    else:
        print("try to type again")
        right_choice()

def upstairs_room():

    print("""You are greeted with 2 choices:
Mysterious left door or casual right door.
Will you choose the left door or the right door?""")

    choice = input("> ")

    if choice == "left":
        mystery_room()
    elif choice == "right":
        gaming_room()
    else:
        print("Try typing something else bruh.")
        upstairs_room()

def gaming_room():

    print("This is the gamer's room. You take a peek at the computer")
    print("""It says "Kungla_game, exit game or start again?""")
    print("Do you wish to exit game or start again?")

    choice = input("> ")

    if "exit" in choice:
        exit(0)
    elif "start" or "again" in choice:
        start()

def mystery_room():

    print("This is indeed a mysterious room.")
    print("You find some money on the cupboard")
    print("You decide to take some.")
    print("The more you take the more chance you have of getting caught")
    print("How much do you wish to take?")

    choice = input("> ")

    while True:
        if ("0" or "1" or "2" or "3" or "4" or "5" or "6" or "7" or "8" or "9" in choice):
            
            how_much = int(choice)
        else:
            print("You have to type only a number here")
            mystery_room()
        
        if how_much < 1000:
            GG("You got the money AND you have enough time to get out")
        else:
            GG("You got caught. U Ded.")
        
start()   