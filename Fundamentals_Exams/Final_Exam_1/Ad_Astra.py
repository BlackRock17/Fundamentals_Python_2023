import re

text = input()

total = 0
result = ""

regex = r"(#|\|)(?P<name>[a-zA-Z\s]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<cal>\d{0,5})\1"

matches = re.finditer(regex, text)

for match in matches:
    result += f"Item: {match.group('name')}, Best before: {match.group('date')}, Nutrition: {match.group('cal')}" + "\n"
    total += int(match.group("cal"))

print(f"You have food to last you for: {total // 2000} days!")
if result:
    print(result)
