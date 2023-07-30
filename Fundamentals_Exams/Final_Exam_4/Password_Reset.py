text = input()

while True:
    command_args = input()

    if command_args == "Done":
        print(f"Your password is: {text}")
        break

    command_args = command_args.split()
    command = command_args[0]

    if command == "TakeOdd":
        new_text = ""
        for idx in range(len(text)):
            if idx % 2 == 1:
                new_text += text[idx]
        text = new_text

    elif command == "Cut":
        index = int(command_args[1])
        length = int(command_args[2])
        text = text[:index] + text[index + length::]

    elif command == "Substitute":
        subs = command_args[1]
        subst = command_args[2]
        if subs in text:
            text = text.replace(subs, subst)
        else:
            print("Nothing to replace!")
            continue

    print(text)


