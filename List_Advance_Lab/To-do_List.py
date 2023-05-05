to_do_note = [0] * 10

while True:
    command = input()

    if command == "End":
        to_do_note = [el for el in to_do_note if el != 0]
        print(to_do_note)
        break

    to_do = command.split("-")
    index = int(to_do[0]) - 1
    to_do_note.pop(index)
    to_do_note.insert(index, to_do[1])







