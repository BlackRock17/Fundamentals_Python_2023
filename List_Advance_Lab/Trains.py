num_wagons = int(input())

wagons = [0] * num_wagons

while True:
    command = input().split()

    if command[0] == "End":
        print(wagons)
        break

    if command[0] == "add":
        wagons[-1] += int(command[1])

    elif command[0] == "insert":
        wagons[int(command[1])] += int(command[2])

    elif command[0] == "leave":
        wagons[int(command[1])] -= int(command[2])

