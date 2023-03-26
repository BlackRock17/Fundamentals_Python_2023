numbers = input().split(" ")
message = input()
message_list = list(message)

text = ""

for i in numbers:
    str_int = [int(i) for i in i]
    index = 0

    for j in range(len(str_int)):
        index += str_int[j]

    index %= len(message_list)
    text += message_list[index]
    message_list.pop(index)

print(text)