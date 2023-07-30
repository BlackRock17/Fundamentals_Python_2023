n = int(input())

heroes = {}

for i in range(n):
    info = input().split()
    heroes[info[0]] = [int(info[1]), int(info[2])]

while True:
    command_args = input()

    if command_args == "End":
        break

    command_args = command_args.split(" - ")
    command = command_args[0]
    hero_name = command_args[1]

    if command == "CastSpell":
        MP_needed = int(command_args[2])
        spell_name = command_args[3]

        if MP_needed <= heroes[hero_name][1]:
            heroes[hero_name][1] -= MP_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {heroes[hero_name][1]} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")

    elif command == "TakeDamage":
        damage = int(command_args[2])
        attacker = command_args[3]

        if heroes[hero_name][0] - damage > 0:
            heroes[hero_name][0] -= damage
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name][0]} HP left!")
        else:
            del heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")

    elif command == "Recharge":
        amount = int(command_args[2])

        current_MP = heroes[hero_name][1]
        heroes[hero_name][1] = min(heroes[hero_name][1] + amount, 200)
        print(f"{hero_name} recharged for {heroes[hero_name][1] - current_MP} MP!")

    else:
        amount = int(command_args[2])

        current_HP = heroes[hero_name][0]
        heroes[hero_name][0] = min(heroes[hero_name][0] + amount, 100)
        print(f"{hero_name} healed for {heroes[hero_name][0] - current_HP} HP!")

for name, value in heroes.items():
    print(name)
    print(f"  HP: {value[0]}")
    print(f"  MP: {value[1]}")


