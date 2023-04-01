def sum(q, name):
    if name == "coffee":
        return q * 1.5
    elif name == "water":
        return q
    elif name == "coke":
        return q * 1.4
    elif name == "snacks":
        return q * 2


product = input()
quantity = int(input())

print(f"{sum(quantity, product):.2f}")

