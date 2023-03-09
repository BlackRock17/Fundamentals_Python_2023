n = int(input())

capacity = 0

for _ in range(n):
    liters = int(input())

    capacity += liters

    if capacity > 255:
        capacity -= liters
        print("Insufficient capacity!")

print(capacity)
