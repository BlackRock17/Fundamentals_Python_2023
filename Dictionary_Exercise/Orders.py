products = {}
products_prc = {}

while True:
    command = input()

    if command == "buy":
        break

    name, price, quantity = command.split(" ")

    if name not in products.keys():
        products[name] = 0
        products_prc[name] = 0

    products[name] += int(quantity)
    products_prc[name] = float(price)

for product, quantity in products.items():
    print(f"{product} -> {quantity * products_prc[product]:.2f}")
