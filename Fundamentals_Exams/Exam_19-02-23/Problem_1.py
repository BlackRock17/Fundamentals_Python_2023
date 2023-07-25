def check_index(index, list_cards):
    if 0 <= index < len(list_cards):
        return True
    return False


cards = input().split(", ")
n = int(input())

for i in range(n):
    action = input().split(", ")
    command = action[0]

    if command == "Add":
        card = action[1]
        if card in cards:
            print("Card is already in the deck")
        else:
            cards.append(card)
            print("Card successfully added")

    elif command == "Remove":
        card = action[1]
        if card not in cards:
            print("Card not found")
        else:
            cards.remove(card)
            print("Card successfully removed")

    elif command == "Remove At":
        index = int(action[1])
        if not check_index(index, cards):
            print("Index out of range")
        else:
            cards.pop(index)
            print("Card successfully removed")

    elif command == "Insert":
        index = int(action[1])
        card = action[2]
        if not check_index(index, cards):
            print("Index out of range")
        elif card in cards:
            print("Card is already added")
        else:
            cards.insert(index, card)
            print("Card successfully added")

print(*cards, sep=", ")


