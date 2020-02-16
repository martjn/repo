some_stuff = "Bread1 Bread2 Bread3 Bread4 Bread5 Bread6"

print(some_stuff)
print("The hell am i supposed to do with this?")
print("Let's make this a list")
 
listed_stuff = some_stuff.split(' ')

print("The result is:")
print(str(listed_stuff))
print("Thats's better.")

extra_stuff = ["Bread7", "Bread8", "Bread9", "Bread10", "Bread11", "Bread12"]


while len(listed_stuff) != 11:
    next_one = extra_stuff.pop()
    print("Adding item: ", next_one)
    listed_stuff.append(next_one)
    print("This is the list now.")
    print(str(listed_stuff))

print("Let's work with these nice breads")

print(listed_stuff[0])
print(listed_stuff[-1])
print("Bread Necklace!", str("-".join(listed_stuff)))
print(listed_stuff[3:9])

