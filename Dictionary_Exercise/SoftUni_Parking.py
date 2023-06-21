n = int(input())

register = {}

for i in range(n):
    command = input().split(" ")

    if len(command) == 2:
        name = command[1]

        if name not in register.keys():
            print(f"ERROR: user {name} not found")
        else:
            del register[name]
            print(f"{name} unregistered successfully")

    elif len(command) == 3:
        name = command[1]
        reg = command[2]

        if name not in register.keys():
            register[name] = reg
            print(f"{name} registered {reg} successfully")
        else:
            print(f"ERROR: already registered with plate number {reg}")

for name, reg in register.items():
    print(f"{name} => {reg}")
