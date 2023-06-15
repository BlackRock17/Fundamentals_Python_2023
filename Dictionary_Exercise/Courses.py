courses = {}

while True:
    command = input()

    if command == "end":
        break

    course, name = command.split(" : ")

    if course not in courses.keys():
        courses[course] = []

    courses[course].append(name)

for course, name in courses.items():
    print(f"{course}: {len(courses[course])}")
    for name in courses[course]:
        print(f"-- {name}")

