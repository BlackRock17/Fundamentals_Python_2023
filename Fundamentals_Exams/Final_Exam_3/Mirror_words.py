import re

text = input()
pairs = 0
mirror = {}

regex = r"(#|@)[A-Za-z]{3,}\1{2}[A-Za-z]{3,}\1"

matches = re.finditer(regex, text)

for match in matches:
    pairs += 1
    if "#" in match[0]:
        info = match[0].split("#")
        if info[1] == info[3][::-1]:
            mirror[info[1]] = info[3]
    else:
        info = match[0].split("@")
        if info[1] == info[3][::-1]:
            mirror[info[1]] = info[3]

if not pairs:
    print("No word pairs found!")
else:
    print(f"{pairs} word pairs found!")

if not mirror:
    print("No mirror words!")
else:
    output = ""
    for key, value in mirror.items():
        output += f"{key} <=> {value}, "
    print("The mirror words are:")
    print(output[:-2])

