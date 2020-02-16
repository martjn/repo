god = 0
bajs = 6
numbers = []

def while_loop(n):
    i = god
    while i < n:
        print(f"At the top i is {i}")
        numbers.append(i)

        i += 1
        print("Numbers now: ", numbers)
        print(f"At the bottom i is {i}")

while_loop(bajs)


print("The numbers: ")

for num in numbers:
    print(num)