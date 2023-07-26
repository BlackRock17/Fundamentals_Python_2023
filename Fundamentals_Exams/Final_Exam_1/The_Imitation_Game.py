from collections import deque

message = deque(list(input()))

while True:
    tokens = input().split("|")
    command = tokens[0]

    if command == "Decode":
        break

    if command == "Move":
        elements = int(tokens[1])
        for i in range(elements):
            message.append(message.popleft())

    elif command == "Insert":
        index = int(tokens[1])
        value = tokens[2]

        for char in reversed(value):
            message.insert(index, char)

    elif command == "ChangeAll":
        subs = tokens[1]
        replacement = tokens[2]
        text = "".join(message)

        while subs in text:
            text = text.replace(subs, replacement)

        message = deque(list(text))

print(f"The decrypted message is: {''.join(message)}")



