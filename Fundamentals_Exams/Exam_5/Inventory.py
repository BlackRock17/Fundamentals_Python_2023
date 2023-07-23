def check_item_exists(item, list_):
    if item in list_:
        return True
    return False

collection = input().split(", ")

while True:
    command = input()

    if command == "Craft!":
        print(*collection, sep=", ")
        break

    command = command.split(" - ")
    action = command[0]

    if action == "Collect":
        item = command[1]
        if not check_item_exists(item, collection):
            collection.append(item)

    elif action == "Drop":
        item = command[1]
        if check_item_exists(item, collection):
            collection.remove(item)

    elif action == "Combine Items":
        old_item, new_item = command[1].split(":")
        if check_item_exists(old_item, collection):
            index = collection.index(old_item)
            collection.insert(index + 1, new_item)

    elif action == "Renew":
        item = command[1]
        if check_item_exists(item, collection):
            collection.remove(item)
            collection.append(item)


