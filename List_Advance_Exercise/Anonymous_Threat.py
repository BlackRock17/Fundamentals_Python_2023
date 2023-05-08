words = input().split()

while True:
    command = input().split()

    if command[0] == "3:1":
        print(*words)
        break

    if command[0] == "merge":
        start = int(command[1])
        end = int(command[2])
        if start < 0:
            start = 0
        if end > len(words) - 1:
            end = len(words) - 1

        for index in range(start + 1, end + 1):
            words[start] += words[index]
        for i in range(start + 1, end + 1):
            words.pop(start + 1)


    elif command[0] == "divide":
        index = int(command[1])
        partitions = int(command[2])

        word = words.pop(index)
        step = len(word) // partitions
        counter = 0

        for i in range(partitions):
            if i == partitions - 1:
                words.insert(index, word[counter::])
            else:
                words.insert(index, word[counter:step + counter])
                counter += step
                index += 1


