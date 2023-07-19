list_of_integers = [int(i) for i in input().split()]

while True:
    command = input().split()

    if command[0] == "end":
        break

    if command[0] == "decrease":
        for index in range(len(list_of_integers)):
            list_of_integers[index] -= 1

    elif command[0] == "swap":
        index_1 = int(command[1])
        index_2 = int(command[2])

        list_of_integers[index_1], list_of_integers[index_2] = list_of_integers[index_2], list_of_integers[index_1]

    elif command[0] == "multiply":
        index_1 = int(command[1])
        index_2 = int(command[2])

        list_of_integers[index_1] *= list_of_integers[index_2]

print(*list_of_integers, sep=", ")