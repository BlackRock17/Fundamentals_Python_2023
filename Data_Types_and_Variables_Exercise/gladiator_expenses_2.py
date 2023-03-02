lost_count = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())

aureus = 0

for lost in range(1, lost_count + 1):

    if lost % 2 == 0:
        aureus += helmet

    if lost % 3 == 0:
        aureus += sword
        if lost % 2 == 0:
            aureus += shield

    if lost % 12 == 0:
        aureus += armor

print(f"Gladiator expenses: {aureus:.2f} aureus")
