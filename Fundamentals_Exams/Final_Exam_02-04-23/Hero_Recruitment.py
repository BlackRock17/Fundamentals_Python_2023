heroes = {}

while True:
    command_args = input()

    if command_args == "End":
        break

    command_args = command_args.split()
    command = command_args[0]
    hero_name = command_args[1]

    if command == "Enroll":
        if hero_name in heroes.keys():
            print(f"{hero_name} is already enrolled.")
        else:
            heroes[hero_name] = []

    elif command == "Learn":
        spell_name = command_args[2]

        if hero_name not in heroes.keys():
            print(f"{hero_name} doesn't exist.")

        elif hero_name in heroes.keys():

            if spell_name in heroes[hero_name]:
                print(f"{hero_name} has already learnt {spell_name}.")

            else:
                heroes[hero_name].append(spell_name)

    elif command == "Unlearn":
        spell_name = command_args[2]

        if hero_name not in heroes.keys():
            print(f"{hero_name} doesn't exist.")

        elif hero_name in heroes.keys():

            if spell_name not in heroes[hero_name]:
                print(f"{hero_name} doesn't know {spell_name}.")

            else:
                heroes[hero_name].remove(spell_name)

print("Heroes:")
for name, spell in heroes.items():
    print(f"== {name}: {', '.join(spell)}")








