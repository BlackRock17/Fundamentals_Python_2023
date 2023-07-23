rooms = input().split("|")

health = 100
bitcoins = 0

for num_room, value in enumerate(rooms, start=1):
    command, points = value.split()
    points = int(points)

    if command == "potion":
        if health + points > 100:
            print(f"You healed for {100 - health} hp.")
            health = 100
        else:
            health += points
            print(f"You healed for {points} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += points
        print(f"You found {points} bitcoins.")

    else:
        health -= points
        if health <= 0:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {num_room}")
            exit(0)
        else:
            print(f"You slayed {command}.")

print("You've made it!")
print(f"Bitcoins: {bitcoins}")
print(f"Health: {health}")


