rows = int(input())
ships = []
for i in range(rows):
    ships.extend([input().split(" ")])

for index in range(len(ships)):
    ships[index] = [int(el) for el in ships[index]]

attacked = input().split(" ")
counter = 0
for attack in attacked:
    row = int(attack[0])
    col = int(attack[2])

    if ships[row][col] <= 0:
        continue
    else:
        ships[row][col] -= 1
        if ships[row][col] == 0:
            counter += 1

print(counter)

