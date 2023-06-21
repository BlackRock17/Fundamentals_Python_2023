students = {}
counter = {}
n = int(input())

for i in range(n):
    name = input()
    grade = float(input())

    if name not in students.keys():
        students[name] = 0
        counter[name] = 0

    students[name] += grade
    counter[name] += 1

for name, grade in students.items():
    if grade / counter[name] >= 4.5:
        print(f"{name} -> {grade / counter[name]:.2f}")
