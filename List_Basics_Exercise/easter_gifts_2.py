gifts = input().split()

while True:
    command = input()

    if command == "No Money":
        break

    command = command.split()

    instruction = command[0]
    gift = command[1]

    if instruction == "OutOfStock":
        for index in range(len(gifts)):
            if gifts[index] == gift:
                gifts[index] = "None"

    elif instruction == "Required":
        index = int(command[2])
        if 0 <= index < len(gifts):
            gifts[index] = gift

    elif instruction == "JustInCase":
        gifts.pop()
        gifts.append(gift)

[print(gift, end= " ")for gift in gifts if gift != "None"]


