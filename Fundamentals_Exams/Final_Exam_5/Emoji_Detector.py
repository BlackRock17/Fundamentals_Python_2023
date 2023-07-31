import re

text = input()

cool_thr = 1

for num in text:
    if num.isdigit():
        cool_thr *= int(num)

regex = r"(:{2}|\*{2})(?P<name>[A-Z][a-z]{2,})\1"

matches = re.finditer(regex, text)

names = {}

for match in matches:
    names[match[0]] = match.group("name")

print(f"Cool threshold: {cool_thr}")
print(f"{len(names)} emojis found in the text. The cool ones are:")

for key, value in names.items():
    cool = 0
    for char in value:
        cool += ord(char)
    if cool > cool_thr:
        print(key)




