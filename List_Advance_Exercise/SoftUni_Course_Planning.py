lessons = input().split(", ")

while True:
    command = input().split(":")

    if command[0] == "course start":
        break

    elif command[0] == "Add":
        if command[1] in lessons:
            continue
        else:
            lessons.append(command[1])

    elif command[0] == "Insert":
        if command[1] in lessons:
            continue
        else:
            lessons.insert(int(command[2]), command[1])

    elif command[0] == "Remove":
        if command[1] in lessons:
            index = lessons.index(command[1])
            if index + 1 in range(len(lessons)):
                if "Exercise" in lessons[index + 1]:
                    lessons.pop(index + 1)

            lessons.remove(command[1])

    elif command[0] == "Swap":
        if command[1] in lessons and command[2] in lessons:
            index_1 = lessons.index(command[1])
            index_2 = lessons.index(command[2])
            lesson_one_exercise = False
            lesson_two_exercise = False
            if index_1 + 1 in range(len(lessons)):
                lesson_one_exercise = "Exercise" in lessons[index_1 + 1]
            if index_2 + 1 in range(len(lessons)):
                lesson_two_exercise = "Exercise" in lessons[index_2 + 1]
            lessons[index_1], lessons[index_2] = lessons[index_2], lessons[index_1]
            if lesson_one_exercise and lesson_two_exercise:
                lessons[index_1 + 1], lessons[index_2 + 1] = \
                lessons[index_2 + 1], lessons[index_1 + 1]
            elif lesson_one_exercise:
                lessons.insert(index_2 + 1, lessons.pop(index_1 + 1))
            elif lesson_two_exercise:
                lessons.insert(index_1 + 1, lessons.pop(index_2 + 1))

    elif command[0] == "Exercise":
        if command[1] in lessons and f"{command[1]}-Exercise" in lessons:
            continue
        elif command[1] in lessons:
            index = lessons.index(command[1])
            lessons.insert(index + 1, f"{command[1]}-Exercise")
        else:
            lessons.append(command[1])
            lessons.append(command[1] + "-Exercise")

counter = 1
for lesson in lessons:
    print(f"{counter}.{lesson}")
    counter += 1

#### SECOND


lessons = input().split(", ")

while True:
    command = input().split(":")

    if command[0] == "course start":
        break

    lesson = command[1]

    if command[0] == "Add":
        if lesson not in lessons:
            lessons.append(lesson)

    elif command[0] == "Insert":
        index = int(command[2])
        if lesson not in lessons:
            lessons.insert(index, lesson)

    elif command[0] == "Remove":
        if lesson in lessons:
            index_exercise = lessons.index(lesson) + 1
            if index_exercise <= len(lessons) - 1:
                if "Exercise" in lessons[index_exercise]:
                    lessons.pop(index_exercise)
            lessons.remove(lesson)

    elif command[0] == "Swap":
        lesson_2 = command[2]

        if lesson in lessons and lesson_2 in lessons:
            index_lesson = lessons.index(lesson)
            index_lesson_2 = lessons.index(lesson_2)
            lessons[index_lesson], lessons[index_lesson_2] = lessons[index_lesson_2], lessons[index_lesson]
            lesson1 = False
            lesson2 = False
            if index_lesson + 1 <= len(lessons) - 1:
                if "Exercise" in lessons[index_lesson + 1]:
                    lesson1 = True

            if index_lesson_2 + 1 <= len(lessons) - 1:
                if "Exercise" in lessons[index_lesson_2 + 1]:
                    lesson2 = True

            if lesson1 and lesson2:
                lessons[index_lesson_2 + 1] = f"{lesson}-Exercise"
                lessons[index_lesson + 1] = f"{lesson_2}-Exercise"
            elif lesson1:
                lessons.pop(index_lesson + 1)
                lessons.insert(index_lesson_2 + 1, f"{lesson}-Exercise")
            elif lesson2:
                lessons.pop(index_lesson_2 + 1)
                lessons.insert(index_lesson + 1, f"{lesson_2}-Exercise")

    elif command[0] == "Exercise":
        if lesson not in lessons:
            lessons.append(lesson)
            lessons.append(f"{lesson}-Exercise")
        else:
            index = lessons.index(lesson) + 1
            if index <= len(lessons) - 1:
                if "Exercise" not in lessons[index]:
                    lessons.insert(index, f"{lesson}-Exercise")
            else:
                lessons.append(f"{lesson}-Exercise")

counter = 1

for lesson in lessons:
    print(f"{counter}.{lesson}")
    counter += 1






