employees = input().split()
happy_factor = int(input())

mid_happiness = 0
happiness = []
counter = 0

for empl in employees:
    mid_happiness += int(empl) * 3 / len(employees)
    happiness.append(int(empl) * 3)

for el in happiness:
    if el >= mid_happiness:
        counter += 1

if len(employees) / 2 <= counter:
    print(f"Score: {counter}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {counter}/{len(employees)}. Employees are not happy!")


