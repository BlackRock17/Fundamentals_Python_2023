def check_total_points(total_points_dict, current_name, current_points):
    if current_name not in total_points_dict.keys():
        total_points_dict[current_name] = current_points

    else:
        total_points_dict[current_name] += current_points

    return total_points_dict


courses = {}
total_points = {}


while True:
    command = input()

    if command == "no more time":
        break

    name, course, points = command.split(" -> ")
    points = int(points)

    if course not in courses.keys():
        courses[course] = {name: points}

        check_total_points(total_points, name, points)

    else:
        if name not in courses[course].keys():
            courses[course][name] = points

            check_total_points(total_points, name, points)

        elif name in courses[course].keys() and courses[course][name] < points:
            total_points[name] += points - courses[course][name]
            courses[course][name] = points

for course_ in courses.keys():
    print(f"{course_}: {len(courses[course_])} participants")
    counter = 1
    sorted_course = sorted(courses[course_].items(), key=lambda x: (-x[1], x[0]))
    for name, value in sorted_course:
        print(f"{counter}. {name} <::> {value}")
        counter += 1


sorted_total_points = dict(sorted(total_points.items(), key=lambda x: (-x[1], x[0])))
counter1 = 1
print("Individual standings:")
for name, t_points in sorted_total_points.items():
    print(f"{counter1}. {name} -> {t_points}")
    counter1 += 1











