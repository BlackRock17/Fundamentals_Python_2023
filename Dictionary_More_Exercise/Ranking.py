from collections import Counter

course_and_pass = {}
name = {}
name_points = {}

while True:
    command = input()

    if command == "end of contests":
        break

    course, password = command.split(":")
    course_and_pass[course] = password

while True:
    command_2 = input()

    if command_2 == "end of submissions":
        break

    current_course, current_pass, user, points = command_2.split("=>")

    if current_course in course_and_pass.keys():
        if course_and_pass[current_course] == current_pass:

            if user not in name.keys():
                name[user] = [current_course + " -> " + points]
                name_points[user] = int(points)
            else:
                found = False
                for el in name[user]:
                    if current_course in el:
                        found = True
                        course_in, points_in = el.split(" -> ")
                        points_in = int(points_in)
                        if points_in < int(points):
                            name[user].append(current_course + " -> " + str(points))
                            name_points[user] += int(points) - points_in
                if not found:
                    name[user].append(current_course + " -> " + points)
                    name_points[user] += int(points)

print(f"Best candidate is {max(name_points)} with total {name_points[max(name_points)]} points.")
print("Ranking:")
for student in sorted(name):
    print(student)
    student_list = {}
    for course in name[student]:
        course_name, max_point = course.split(" -> ")
        max_point = int(max_point)
        student_list[course_name] = max_point
    sort_student_list = dict(sorted(student_list.items(), key=lambda item: item[1]))

    c = Counter(sort_student_list)

    for p in c.most_common():
        print(f"#  {p[0]} -> {p[1]}")





