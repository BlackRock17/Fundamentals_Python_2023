students = {}
counter = {}
while True:
    command = input()

    if command == "exam finished":
        break

    info = command.split("-")

    if len(info) == 3:
        name = info[0]
        language = info[1]
        points = int(info[2])

        if name not in students.keys():
            students[name] = points
        else:
            if students[name] < points:
                students[name] = points

        if language not in counter.keys():
            counter[language] = 0
        counter[language] += 1

    elif len(info) == 2:
        name = info[0]

        if name in students.keys():
            del students[name]

print("Results:")
for name, points in students.items():
    print(f"{name} | {points}")
print("Submissions:")
for language, points in counter.items():
    print(f"{language} - {points}")


