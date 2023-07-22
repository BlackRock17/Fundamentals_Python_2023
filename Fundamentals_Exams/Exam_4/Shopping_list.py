products = input().split("!")

while True:
    tokens = input()

    if tokens == "Go Shopping!":
        break

    tokens = tokens.split()
    command = tokens[0]
    item = tokens[1]

    if command == "Urgent":
        if item not in products:
            products.insert(0, item)

    elif command == "Unnecessary":
        if item in products:
            products.remove(item)

    elif command == "Correct":
        new_item = tokens[2]
        if item in products:
            index = products.index(item)
            products[index] = new_item

    elif command == "Rearrange":
        if item in products:
            products.remove(item)
            products.append(item)

print(*products, sep=", ")


