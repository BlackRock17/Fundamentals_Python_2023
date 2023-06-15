force_book = {}

while True:
    command = input()

    if command == "Lumpawaroo":
        break

    if "|" in command:
        side, user = command.split(" | ")
        found = False

        for el in force_book.keys():
            if user in force_book[el]:
                found = True

        if found:
            continue

        if side not in force_book.keys():
            force_book[side] = []
        force_book[side].append(user)

    elif "->" in command:
        user, side = command.split(" -> ")

        for el in force_book.keys():
            if user in force_book[el]:
                force_book[el].remove(user)

        if side in force_book.keys():
            force_book[side].append(user)
        else:
            force_book[side] = []
            force_book[side].append(user)
        print(f"{user} joins the {side} side!")

for side in force_book.keys():
    if len(force_book[side]) > 0:
        print(f"Side: {side}, Members: {len(force_book[side])}")
        for user in force_book[side]:
            print(f"! {user}")



