people = int(input())
wagons = [int(x) for x in input().split()]

for wagon in wagons:
    if wagon >= 4:
        continue
    else:
        index = wagons.index(wagon)
        free_space = 4 - wagon

    if people < free_space:
        wagons[index] += people
        people = 0
        break

    else:
        wagons[index] += 4 - wagon
        people -= 4 - wagon

if not people and wagons[-1] == 4:
    print(*wagons, sep=" ")

elif people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(*wagons, sep=" ")

else:
    print("The lift has empty spots!")
    print(*wagons, sep=" ")

