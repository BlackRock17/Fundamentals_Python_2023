import re

text = input()

regex = r"\b_[A-Za-z]+\b"

matches = re.finditer(regex, text, re.MULTILINE)

output = []

for matchNum, match in enumerate(matches, start=1):
    output.append(match[0][1:])

print(*output, sep=",")