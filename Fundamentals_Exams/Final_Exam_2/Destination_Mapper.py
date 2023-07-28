import re

text = input()

pattern = r"(=|/)(?P<name>[A-Z][A-Za-z]{2,})\1"

destination = []

matches = re.finditer(pattern, text)

for match in matches:
    destination.append(match.group("name"))

if not destination:
    print("Destinations:")
    print("Travel Points: 0")
else:
    print(f"Destinations: {', '.join(destination)}")
    print(f"Travel Points: {sum([len(points) for points in destination])}")
