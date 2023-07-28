from collections import deque

N = int(input())

plants = {}

for _ in range(N):
    plant, rarity = input().split("<->")
    plants[plant] = deque([rarity])

while True:
    info = input()

    if info == "Exhibition":
        break

    info = info.split(": ")
    command = info[0]

    if command == "Rate":
        name, rate = info[1].split(" - ")
        if name not in plants.keys():
            print("error")
            continue
        rate = int(rate)
        plants[name].append(rate)

    elif command == "Update":
        name, new_rarity = info[1].split(" - ")
        if name not in plants.keys():
            print("error")
            continue
        plants[name][0] = new_rarity

    elif command == "Reset":
        name = info[1]
        if name not in plants.keys():
            print("error")
            continue
        plants[name] = deque([plants[name][0]])

print("Plants for the exhibition:")
for key, value in plants.items():
    print(f"- {key}; Rarity: {value.popleft()}; Rating: {sum(value) / len(value) if value else 0.00:.2f}")
