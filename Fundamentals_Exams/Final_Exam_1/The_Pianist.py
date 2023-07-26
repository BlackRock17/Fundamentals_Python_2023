N = int(input())

result = {}

for _ in range(N):
    info = input().split("|")
    result[info[0]] = [info[1], info[2]]

while True:
    inf = input().split("|")
    command = inf[0]

    if command == "Stop":
        break

    piece = inf[1]

    if command == "Add":
        composer = inf[2]
        key = inf[3]
        if piece in result.keys():
            print(f"{piece} is already in the collection!")
        else:
            result[piece] = [composer, key]
            print(f"{piece} by {composer} in {key} added to the collection!")

    elif command == "Remove":
        if piece in result.keys():
            del result[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif command == "ChangeKey":
        new_key = inf[2]
        if piece in result.keys():
            result[piece][1] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

for key, value in result.items():
    print(f"{key} -> Composer: {value[0]}, Key: {value[1]}")
