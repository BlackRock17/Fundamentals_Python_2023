import re

number = int(input())
regex = r"(^)(\$|\%)(?P<name>[A-Z][a-z]{2,})\2: (?P<digit>\[\d+]\|\[\d+]\|\[\d+]\|)$"

for el in range(number):
    text = input()

    matches = re.finditer(regex, text)
    message = ""
    for match in matches:
        name = match.group("name")
        info = match.group("digit")
        info = info.split("|")

        for idx in range(3):
            num = int(info[idx][1:-1])
            message += chr(num)

        print(f"{name}: {message}")
        break

    else:
        print("Valid message not found!")





