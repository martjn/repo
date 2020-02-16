ten_things = "Apples Oragnes Cows Telephone Light Sugar"

print("First off it's this: " + ten_things)

print("Wait there are not 10 things in that list. Let's fix it.")

stuff = ten_things.split(' ')
print("Secondly it's this:", stuff)
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop() # pop(more_stuff) call pop with argument more_stuff
    print("Adding: ", next_one)
    stuff.append(next_one) # append(stuff, next_one) call append with arguments stuff and next_one
    print(f"There are {len(stuff)} items now.")     

print("There we go: ", stuff)

print("Let's do some things with stuff")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff)) # join(stuff, ' ')
print('#'.join(stuff[3:10]))