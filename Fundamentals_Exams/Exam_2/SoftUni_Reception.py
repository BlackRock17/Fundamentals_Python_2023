help_per_hour = 0

for i in range(3):
    help_per_hour += int(input())

students = int(input())
counter = 0
time = 0

while students > 0:
    counter += 1

    if counter == 4:
        counter = 0
        time += 1
        continue
    else:
        students -= help_per_hour
        time += 1

print(f"Time needed: {time}h.")



