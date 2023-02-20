while True:
    command = input()

    if command == "End":
        break

    if command == "SoftUni":
        continue

    text = ""

    for char in command:
        text += char * 2

    print(f"{text}")


