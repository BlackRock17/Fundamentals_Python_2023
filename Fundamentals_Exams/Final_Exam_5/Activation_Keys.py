text = input()

while True:
    command_args = input()

    if command_args == "Generate":
        break

    command_args = command_args.split(">>>")
    command = command_args[0]

    if command == "Contains":
        substring = command_args[1]

        if substring in text:
            print(f"{text} contains {substring}")
        else:
            print("Substring not found!")

    elif command == "Flip":
        up_low = command_args[1]
        start_idx = int(command_args[2])
        end_idx = int(command_args[3])

        if up_low == "Upper":
            text = text[:start_idx] + text[start_idx:end_idx].upper() + text[end_idx::]
        else:
            text = text[:start_idx] + text[start_idx:end_idx].lower() + text[end_idx::]

        print(text)

    elif command == "Slice":
        start_idx = int(command_args[1])
        end_idx = int(command_args[2])

        text = text[:start_idx] + text[end_idx::]

        print(text)

print(f"Your activation key is: {text}")