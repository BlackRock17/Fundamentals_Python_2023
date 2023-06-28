import re

text = input()

matches = re.finditer(r"(^|(?<=\s))-?([0]|[1-9]*)(\.\d+)?($|(?=\s))", text)

for match in matches:
    print(match.group(), end=" ")