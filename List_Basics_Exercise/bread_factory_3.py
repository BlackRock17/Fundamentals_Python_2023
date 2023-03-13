days_events = input().split("|")

energy = 100
coins = 100
complete = True

for i in days_events:
    event, number = i.split("-")
    number = int(number)

    if event == "rest":
        if energy + number > 100:
            print(f"You gained {100 - energy} energy.")
            energy = 100
        else:
            energy += number
            print(f"You gained {number} energy.")
        print(f"Current energy: {energy}.")

    elif event == "order":
        if energy < 30:
            energy += 50
            print("You had to rest!")
        else:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")

    else:
        if number > coins:
            print(f"Closed! Cannot afford {event}.")
            complete = False
            break
        else:
            coins -= number
            print(f"You bought {event}.")

if complete:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")




