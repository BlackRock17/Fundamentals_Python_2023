counter = 0

while True:
    command = input()

    if command == "END":
        break

    if command.isupper():
        if command == "CODING" or command == "DOG" or command == "CAT" or command == "MOVIE":
            counter += 2
        else:
            continue
    elif command.islower():
        if command == "coding" or command == "dog" or command == "cat" or command == "movie":
            counter += 1
        else:
            continue

if counter < 6:
    print(counter)
else:
    print("You need extra sleep")
