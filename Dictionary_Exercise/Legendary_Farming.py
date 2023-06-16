materials = input().split(" ")
result = {"shards": 0, "fragments": 0, "motes": 0}

key_win = ""
win = False
while not win:
    for index in range(0, len(materials), 2):
        materials[index + 1] = materials[index + 1].lower()
        if materials[index + 1] not in result:
            result[materials[index + 1]] = 0
        result[materials[index + 1]] += int(materials[index])

        if result[materials[index + 1]] >= 250 and key_win == "":
            if materials[index + 1] == "shards" \
                or materials[index + 1] == "fragments" \
                or materials[index + 1] == "motes":
                key_win = materials[index + 1]
                result[materials[index + 1]] -= 250
                win = True
                break
    if win:
        break
    materials = input().split(" ")

if key_win == "shards":
    print("Shadowmourne obtained!")
elif key_win == "fragments":
    print("Valanyr obtained!")
elif key_win == "motes":
    print("Dragonwrath obtained!")

for material, quantity in result.items():
    print(f"{material}: {quantity}")

