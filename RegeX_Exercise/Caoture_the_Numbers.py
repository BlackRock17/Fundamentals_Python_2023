import re

while True:
    text = input()

    if not text:
        break

    regex = r"\d+"

    matches = re.finditer(regex, text, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        print(match[0], end=" ")


