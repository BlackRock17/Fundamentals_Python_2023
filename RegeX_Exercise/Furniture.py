import re

total = 0
names = []

while True:
    command = input()

    if command == "Purchase":
        break

    regex = r"^>{2}(?P<furniture>[A-Za-z]+)<{2}(?P<price>\d+([.]\d+)?)!(?P<quantity>\d+)"

    matches = re.finditer(regex, command, re.IGNORECASE)

    for match in matches:
        names.append(match.group("furniture"))
        price = float(match.group("price"))
        quantity = int(match.group("quantity"))
        total += price * quantity

print("Bought furniture:")
for name in names:
    print(name)
print(f"Total money spend: {total:.2f}")

