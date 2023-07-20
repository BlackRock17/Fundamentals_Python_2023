integers = [int(i) for i in input().split()]
count = 0

while True:
    command = input()

    if command == "End":
        print(f"Shot targets: {count} ->", end=" ")
        print(*integers, sep=" ")
        break

    index = int(command)

    if index < 0 or index > len(integers) - 1 or integers[index] == -1:
        continue

    value = integers[index]
    integers[index] = -1
    count += 1

    for num_index in range(len(integers)):
        if integers[num_index] != -1:
            if integers[num_index] > value:
                integers[num_index] -= value
            else:
                integers[num_index] += value



