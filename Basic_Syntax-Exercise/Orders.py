orders = int(input())

total = 0

for i in range(orders):
    capsule_prc = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if capsule_prc < 0.01 or days < 1 or capsules_per_day < 1:
        continue
    elif capsule_prc > 100 or days > 31 or capsules_per_day > 2000:
        continue

    total_order = capsule_prc * days * capsules_per_day
    total += total_order

    print(f"The price for the coffee is: ${total_order:.2f}")

print(f"Total: ${total:.2f}")