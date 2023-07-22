houses = [int(i) for i in input().split("@")]

last_index = 0
while True:
    command = input()

    if command == "Love!":
        break

    command = command.split()
    index = int(command[1]) + last_index

    if index > len(houses) - 1:
        index = 0

    if houses[index] == 0:
        print(f"Place {index} already had Valentine's day.")
    else:
        houses[index] -= 2
        if houses[index] == 0:
            print(f"Place {index} has Valentine's day.")

    last_index = index

print(f"Cupid's last position was {last_index}.")

counter = 0
for el in houses:
    if el != 0:
        counter += 1

if counter == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {counter} places.")
