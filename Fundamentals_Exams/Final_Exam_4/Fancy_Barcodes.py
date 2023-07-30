import re

n = int(input())
regex = r"@#+([A-Z][A-Za-z0-9]{4,}[A-Z])@#+"


for i in range(n):
    barcode = input()

    codes = re.findall(regex, barcode)
    if not codes:
        print("Invalid barcode")
        continue

    number = []

    for num in codes[0]:
        try:
            a = int(num)
            number.append(num)
        except ValueError:
            pass

    if number:
        print(f"Product group: {''.join(number)}")
    else:
        print("Product group: 00")






