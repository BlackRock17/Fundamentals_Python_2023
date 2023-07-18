def insert_elements(list_elements):
    middle = int(len(elements) / 2)
    list_elements.insert(middle, f"-{counter}a")
    list_elements.insert(middle + 1, f"-{counter}a")
    print("Invalid input! Adding additional elements to the board")
    return list_elements


elements = input().split()
counter = 0

while True:
    command = input()

    if command == "end":
        break

    counter += 1

    command = command.split(" ")

    if command[0] == command[1]:
        insert_elements(elements)
        continue

    index1 = int(command[0])
    index2 = int(command[1])

    if index1 < 0 or index1 > len(elements) - 1 or index2 < 0 or index2 > len(elements) - 1:
        insert_elements(elements)
        continue

    if elements[index1] == elements[index2]:
        el = elements[index1]
        elements.remove(el)
        elements.remove(el)
        print(f"Congrats! You have found matching elements - {el}!")

    elif elements[index1] != elements[index2]:
        print("Try again!")

    if not elements:
        print(f"You have won in {counter} turns!")
        break

if elements:
    print("Sorry you lose :(")
    print(*elements, sep=" ")



