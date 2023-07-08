participants = input().split(", ")
result = {}

while True:
    text = input()

    if text == "end of race":
        break

    name = ""
    distance = 0

    for el in text:
        if el.isalpha():
            name += el
        elif el.isdigit():
            distance += int(el)

    if name in participants:
        if name in result.keys():
            result[name] += distance
        else:
            result[name] = distance

sorted_result = dict(sorted(result.items(), key=lambda x: x[1], reverse=True))

list_ = []

counter = 0
for name in sorted_result:
    list_.append(name)
    counter += 1
    if counter == 3:
        break

print(f"1st place: {list_[0]}")
print(f"2nd place: {list_[1]}")
print(f"3rd place: {list_[2]}")



