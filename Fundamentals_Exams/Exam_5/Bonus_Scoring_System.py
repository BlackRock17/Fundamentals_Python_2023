from math import ceil

students = int(input())
lectures = int(input())
bonus = int(input())

attendance_list = []
for _ in range(students):
    num = int(input())
    attendance_list.append(num)

if attendance_list:
    max_attendance = max(attendance_list)

    total_bonus = max_attendance / lectures * (5 + bonus)

    print(f"Max Bonus: {ceil(total_bonus)}.")
    print(f"The student has attended {max_attendance} lectures.")

else:
    print(f"Max Bonus: 0.")
    print(f"The student has attended 0 lectures.")


