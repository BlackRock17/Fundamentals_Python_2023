text = input()

while True:
    info = input()

    if info == "Finish":
        break

    info = info.split()
    command = info[0]

    if command == "Replace":
        current_char = info[1]
        new_char = info[2]

        text = text.replace(current_char, new_char)
        print(text)

    elif command == "Cut":
        start_idx = int(info[1])
        end_idx = int(info[2])

        if 0 <= start_idx < len(text) and 0 <= end_idx < len(text):
            text = text[:start_idx] + text[end_idx + 1::]
            print(text)
        else:
            print("Invalid indices!")

    elif command == "Make":
        Up_Low = info[1]

        if Up_Low == "Upper":
            text = text.upper()
        else:
            text = text.lower()

        print(text)

    elif command == "Check":
        string = info[1]

        if string in text:
            print(f"Message contains {string}")
        else:
            print(f"Message doesn't contain {string}")

    elif command == "Sum":
        start_idx = int(info[1])
        end_idx = int(info[2])
        sum = 0

        if 0 <= start_idx < len(text) and 0 <= end_idx < len(text):
            text_info = text[start_idx:end_idx + 1]
            for char in text_info:
                sum += int(ord(char))
            print(sum)

        else:
            print("Invalid indices!")



