teams = {"A": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], "B": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]}

info = input().split(" ")
stop = False

for i in info:
    team, number = i.split("-")
    number = int(number)

    if team == "A":
        if number in teams[team]:
            teams[team].remove(number)
    elif team == "B":
        if number in teams[team]:
            teams[team].remove(number)

    if len(teams["A"]) < 7 or len(teams["B"]) < 7:
        stop = True
        break

print(f"Team A - {len(teams['A'])}; Team B - {len(teams['B'])}")
if stop:
    print("Game was terminated")

