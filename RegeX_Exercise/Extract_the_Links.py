import re
regex = r"\bwww\.[A-Za-z0-9-]+\.[a-z]+(\.[a-z]+)*\b"

text = input()
while text:
    matches = re.finditer(regex, text, re.IGNORECASE)

    for matchNum, match in enumerate(matches, start=1):
        print(match[0])

    text = input()