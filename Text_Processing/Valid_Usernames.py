usernames = input().split(", ")

for word in usernames:
    valid = True
    if len(word) < 3 or len(word) > 16:
        valid = False

    for el in word:
        if not el.isalnum():
            if not el == "-":
                if not el == "_":
                    valid = False

    if valid:
        print(word)


