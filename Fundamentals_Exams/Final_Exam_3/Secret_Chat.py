text = input()

while True:
    info = input()

    if info == "Reveal":
        break

    info = info.split(":|:")
    command = info[0]

    if command == "InsertSpace":
        idx = int(info[1])
        text = text[:idx] + " " + text[idx::]
        print(text)

    elif command == "Reverse":
        subs = info[1]
        if subs in text:
            idx = text.find(subs)
            text = text[:idx] + text[idx + len(subs)::] + subs[::-1]
            print(text)
        else:
            print("error")

    elif command == "ChangeAll":
        subs = info[1]
        repl = info[2]

        text = text.replace(subs, repl)
        print(text)

print(f"You have a new text message: {text}")



