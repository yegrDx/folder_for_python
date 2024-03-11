import random as rd
goatCounter = 0
carCounter = 0
n = 1e6
for i in range(int(n)):
    doors = ["goat"]*3
    doors[rd.randint(0,2)] = "car"

    if doors[1] == "goat":
        doors.pop(1)
    elif doors[2] == "goat":
        doors.pop(2)
    chosenDoor = doors[1]

    if chosenDoor == "car":
        carCounter += 1
    else:
        goatCounter += 1

print(carCounter/n)
print(goatCounter/n)