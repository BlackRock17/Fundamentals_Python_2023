import re

test_str = input()
search_word = input()

regex = rf"\b{search_word}\b"

matches = re.finditer(regex, test_str, re.IGNORECASE)

counter = 0
for matchNum, match in enumerate(matches, start=1):
    counter += 1

print(counter)