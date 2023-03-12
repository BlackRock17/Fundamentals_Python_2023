working_day = input().split("|")

energy = 100
coins = 100
completed = False

for i in working_day:
    event = i.split("-")
    order = event[0]
    number = int(event[1])

    if order == "rest":
        if number + energy > 100:
            gained_energy = 100 - energy
            energy = 100

        else:
            energy += number
            gained_energy = number

        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")

    elif order == "order":
        if energy < 30:
            energy += 50
            print("You had to rest!")
            continue
        else:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")

    else:
        if coins < number:
            print(f"Closed! Cannot afford {order}.")
            break
        else:
            coins -= number
            print(f"You bought {order}.")

    if i == working_day[-1]:
        completed = True

if completed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")


