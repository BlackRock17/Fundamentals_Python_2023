companies = {}

while True:
    command = input()

    if command == "End":
        break

    name, id = command.split(" -> ")

    if name not in companies.keys():
        companies[name] = []

    if id not in companies[name]:
        companies[name].append(id)

for name, id in companies.items():
    print(name)
    for id in companies[name]:
        print(f"-- {id}")
