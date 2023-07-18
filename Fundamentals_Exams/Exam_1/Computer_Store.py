total = 0

while True:
    command = input()

    if command == "special" or command == "regular":
        break

    price = float(command)

    if price <= 0:
        print("Invalid price!")
    else:
        total += price

if total < 1:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {total:.2f}$")
    print(f"Taxes: {total * 0.2:.2f}$")
    print("-----------")

    if command == "special":
        print(f"Total price: {(total + (total * 0.2)) * 0.9:.2f}$")
    else:
        print(f"Total price: {total + (total * 0.2):.2f}$")

