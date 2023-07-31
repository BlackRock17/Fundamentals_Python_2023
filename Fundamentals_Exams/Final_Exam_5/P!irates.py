towns_population = {}
towns_gold = {}

while True:
    info = input()

    if info == "Sail":
        break

    info = info.split("||")
    if info[0] in towns_population.keys():
        towns_population[info[0]] += int(info[1])
        towns_gold[info[0]] += int(info[2])
    else:
        towns_population[info[0]] = int(info[1])
        towns_gold[info[0]] = int(info[2])

while True:
    command_args = input()

    if command_args == "End":
        break

    command_args = command_args.split("=>")
    command = command_args[0]
    town = command_args[1]

    if command == "Plunder":
        people = int(command_args[2])
        gold = int(command_args[3])
        print(f"{town} plundered! {min(towns_gold[town], gold)} gold stolen, {min(towns_population[town], people)} citizens killed.")

        towns_population[town] -= people
        towns_gold[town] -= gold

        if towns_population[town] < 1 or towns_gold[town] < 1:
            del towns_population[town]
            del towns_gold[town]
            print(f"{town} has been wiped off the map!")

    elif command == "Prosper":
        gold = int(command_args[2])

        if gold < 1:
            print("Gold added cannot be a negative number!")
        else:
            towns_gold[town] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {towns_gold[town]} gold.")

if towns_population:
    print(f"Ahoy, Captain! There are {len(towns_population)} wealthy settlements to go to:")
    for key, value in towns_population.items():
        print(f"{key} -> Population: {value} citizens, Gold: {towns_gold[key]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")




