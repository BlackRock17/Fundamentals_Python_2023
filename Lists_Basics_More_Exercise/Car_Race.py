timer = [int(x) for x in input().split()]

time_left_car = 0
time_right_car = 0

half = int(len(timer) / 2)

for left_car in range(0, half):
    if timer[left_car] == 0:
        time_left_car *= 0.8
    else:
        time_left_car += timer[left_car]

for right_car in range(len(timer) -1, half, -1):
    if timer[right_car] == 0:
        time_right_car *= 0.8
    else:
        time_right_car += timer[right_car]


if time_left_car < time_right_car:
    print(f"The winner is left with total time: {time_left_car:.1f}")
else:
    print(f"The winner is right with total time: {time_right_car:.1f}")



