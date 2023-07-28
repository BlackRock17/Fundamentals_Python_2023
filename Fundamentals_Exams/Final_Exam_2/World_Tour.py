text = input()

while True:
    info = input()

    if info == "Travel":
        break

    info = info.split(":")
    command = info[0]

    if command == "Add Stop":
        index = int(info[1])
        string = info[2]

        if 0 <= index <= len(text) - 1:
            first_half = text[:index] + string
            second_half = text[index::]
            text = first_half + second_half

    elif command == "Remove Stop":
        start_index = int(info[1])
        end_index = int(info[2])

        if 0 <= start_index <= len(text) - 1 and 0 <= end_index <= len(text) - 1 and start_index <= end_index:
            text = text[:start_index] + text[end_index + 1::]

    elif command == "Switch":
        old_string = info[1]
        new_string = info[2]

        if old_string in text:
            text = text.replace(old_string, new_string)

    print(text)

print(f"Ready for world tour! Planned stops: {text}")
