print("""You enter the main house of Kungla talu.
This is the house tour of Kungla talu. Do you go with door
on your right(#1) or walk forward(#2)?""")

option1 = input("> ")

if option1 == "1":
    print("""This is the bathroom. You have reached the end of
house tour for now""")
    quit()
elif option1 == "2":
    print("""You have now reached the kitchen.
You can, from here, go to your left(#1) or upstairs(#2)
what will you choose?""")

    option2 = input("> ")

if option2 == "1":
    print("""You have now reached the living room.
You have no choice but to go forward.
enter another room, doesn't seem much.
You now enter the fireplace room. You can go to your
right where's a door(#1) or to your left(#2).
what will you choose?""")

    option3 = input("> ")

    if option3 == "1":
        print("""You have reached the sauna room. nothing much
here. And thus completed the journey.""")
        quit()

    elif option3 == "2":
        print("""You have reached the backdoor. Nothing much
here, and thus have completed the journey.""")
        quit()

elif option2 == "2":

    print("""You have reached upstairs. You have the choice
of going to your right(#1), which is the room i 
mostly spend my time in, or to your left(#2),
where's my parents room. What will you choose?""")

    option4 = input("> ")

    if option4 == "1":
        print("""You have reached the room i spend my time
in most. Hi Martyn! You have nothing else to discover,
and thus have completed the journey.""")
        quit()
    elif option4 == "2":
        print("""This the parents room. Nothing of interest
in here. Thus you have completed the journey.""")
        quit()


