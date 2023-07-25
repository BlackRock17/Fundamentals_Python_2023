experience = float(input())
battles = int(input())

total = 0
win = False
for battle in range(1, battles + 1):
    number = float(input())

    total += number

    if battle % 3 == 0:
        total += number * 0.15

    if battle % 5 == 0:
        total -= number * 0.1

    if battle % 15 == 0:
        total += number * 0.5

    if total >= experience:
        print(f"Player successfully collected his needed experience for {battle} battles.")
        win = True
        break

if not win:
    print(f"Player was not able to collect the needed experience, {experience - total:.2f} more needed.")
