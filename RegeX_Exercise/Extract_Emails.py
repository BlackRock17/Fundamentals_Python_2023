import re

regex = r"( |^)[A-Za-z0-9]+([-._])?([A-Za-z0-9]+)?@[A-Za-z]+([-][A-Za-z]+)?[.][A-Za-z]+([.][A-Za-z]+)?"

test_str = input()

matches = re.finditer(regex, test_str, re.IGNORECASE)

for matchNum, match in enumerate(matches, start=1):
    print(match[0])
