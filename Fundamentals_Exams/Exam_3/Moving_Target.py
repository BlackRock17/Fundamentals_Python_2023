targets = [int(i) for i in input().split()]

while True:
    command = input()

    if command == "End":
        break

    command = command.split()
    task = command[0]
    index = int(command[1])
    value = int(command[2])

    if task == "Shoot" and 0 <= index < len(targets):
        if value >= targets[index]:
            targets.pop(index)
        else:
            targets[index] -= value

    elif task == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")

    elif task == "Strike":
        if 0 <= index - value and index + value < len(targets):
            del targets[index - value: index + value + 1]
        else:
            print("Strike missed!")

print(*targets, sep="|")
