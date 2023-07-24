treasure_list = input().split("|")

while True:
    command = input()

    if command == "Yohoho!":
        break

    command = command.split()
    action = command.pop(0)

    if action == "Loot":
        for el in command:
            if el not in treasure_list:
                treasure_list.insert(0, el)

    elif action == "Drop":
        index = int(command[0])
        if 0 <= index < len(treasure_list):
            loot = treasure_list.pop(index)
            treasure_list.append(loot)

    elif action == "Steal":
        count = int(command[0])
        if count > len(treasure_list):
            count = len(treasure_list)

        del_el = []
        for i in range(count):
            del_el.append(treasure_list.pop())
        if del_el:
            del_el.reverse()
            print(*del_el, sep=", ")

if not treasure_list:
    print("Failed treasure hunt.")
else:
    gain = 0

    for name in treasure_list:
        gain += len(name)

    average_gain = gain / len(treasure_list)

    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")

