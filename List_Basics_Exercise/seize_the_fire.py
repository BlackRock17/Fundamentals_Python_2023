fires_cells = input().split("#")
water = int(input())

cells = []
total_fire = 0
effort = 0

for i in fires_cells:
    fire_info = i.split(" = ")
    type = fire_info[0]
    value = int(fire_info[1])

    if type == "High" and 81 <= value <= 125 and water >= value:
        water -= value
        total_fire += value
        effort += value * 0.25
        cells.append(value)
    elif type == "Medium" and 51 <= value <= 80 and water >= value:
        water -= value
        total_fire += value
        effort += value * 0.25
        cells.append(value)
    elif type == "Low" and 1 <= value <= 50 and water >= value:
        water -= value
        total_fire += value
        effort += value * 0.25
        cells.append(value)

print("Cells:")
for j in cells:
    print(f" - {j}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")

#### SECOND SOLUTION

fires = input().split("#")
water = int(input())
total_fire = 0
fires_count = []

for fire in fires:
    type, level = fire.split(" = ")
    level = int(level)
    if water < level:
        continue

    if type == "High":
        if 81 <= level < 126:
            total_fire += level
            fires_count.append(level)
            water -= level

    elif type == "Medium":
        if 50 < level < 81:
            total_fire += level
            fires_count.append(level)
            water -= level

    elif type == "Low":
        if 0 < level < 51:
            total_fire += level
            fires_count.append(level)
            water -= level

print("Cells:")
[print(f" - {fire}", sep='\n') for fire in fires_count]
print(f"Effort: {total_fire * 0.25:.2f}")
print(f"Total Fire: {total_fire}")



