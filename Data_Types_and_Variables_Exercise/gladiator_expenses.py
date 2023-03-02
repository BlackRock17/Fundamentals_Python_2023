fight_lost = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())

total = 0
shield_counter = 0

for fight in range(1, fight_lost + 1):

    if fight % 2 == 0:
        total += helmet

    if fight % 3 == 0:
        total += sword

    if fight % 2 == 0 and fight % 3 == 0:
        total += shield
        shield_counter += 1

    if shield_counter == 2:
        total += armor
        shield_counter = 0

print(f"Gladiator expenses: {total:.2f} aureus")



