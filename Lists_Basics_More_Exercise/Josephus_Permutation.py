person_num = input().split()
num_execution = int(input())

executed = []
counter = 0
index = 0

while len(person_num) != 0:
    counter += 1

    if counter % num_execution == 0:
        executed.append(person_num[index])
        person_num.pop(index)
    else:
        index += 1

    if index == len(person_num):
        index = 0

executed = ",".join(executed)

print(f"[{executed}]")


