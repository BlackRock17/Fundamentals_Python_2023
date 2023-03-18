items = input().split("|")
budget = float(input())

new_prices = []
profit = 0

for item in items:
    article, price = item.split("->")
    price = float(price)

    if article == "Clothes" and price > 50:
        continue
    elif article == "Shoes" and price > 35:
        continue
    elif article == "Accessories" and price > 20.5:
        continue
    elif price > budget:
        continue

    budget -= price
    new_price = round(price * 1.4, 2)
    profit += new_price - price
    new_prices.append(new_price)

for prc in new_prices:
    budget += prc
    print(f"{prc:.2f}", end=" ")
print("")
print(f"Profit: {profit:.2f}")
if budget >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
