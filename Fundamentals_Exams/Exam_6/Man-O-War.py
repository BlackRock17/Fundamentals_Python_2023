def valid_index(index, list_):
    if 0 <= index < len(list_):
        return True
    return False

pirate_ship = [int(x) for x in input().split(">")]
warship = [int(x) for x in input().split(">")]
health_capacity = int(input())

while True:
    command = input()

    if command == "Retire":
        break

    command = command.split()
    action = command[0]

    if action == "Fire":
        index = int(command[1])
        damage = int(command[2])
        if valid_index(index, warship):
            warship[index] -= damage
            if warship[index] <= 0:
                print("You won! The enemy ship has sunken.")
                exit(0)

    elif action == "Defend":
        start_index = int(command[1])
        end_index = int(command[2])
        damage = int(command[3])

        if valid_index(start_index, pirate_ship) and valid_index(end_index, pirate_ship):
            for idx in range(start_index, end_index + 1):
                pirate_ship[idx] -= damage
                if pirate_ship[idx] <= 0:
                    print("You lost! The pirate ship has sunken.")
                    exit(0)

    elif action == "Repair":
        index = int(command[1])
        health = int(command[2])

        if valid_index(index, pirate_ship):
            pirate_ship[index] = min(health_capacity, pirate_ship[index] + health)

    elif action == "Status":
        counter = 0
        for section in pirate_ship:
            if section < health_capacity * 0.2:
                counter += 1
        print(f"{counter} sections need repair.")

print(f"Pirate ship status: {sum(pirate_ship)}")
print(f"Warship status: {sum(warship)}")

