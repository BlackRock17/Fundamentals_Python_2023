import re

total = 0

while True:
    command = input()

    if command == "end of shift":
        break

    name = r"(?<=%)[A-Z][a-z]+(?=%)"
    product = r"(?<=<)\w+(?=>)"
    count = r"(?<=\|)\d+(?=\|)"
    price = r"\d+(\.\d+)?(?=\$)"

    match_name = re.findall(name, command)
    match_product = re.findall(product, command)
    match_count = re.findall(count, command)
    match_price = re.finditer(price, command)
    match_price_ = []

    for match in match_price:
        match_price_.append(match.group())

    if not match_name or not match_product or not match_count or not match_price_:
        continue
    else:
        print(f"{match_name[0]}: {match_product[0]} - {int(match_count[0]) * float(match_price_[0]):.2f}")
        total += int(match_count[0]) * float(match_price_[0])

print(f"Total income: {total:.2f}")



