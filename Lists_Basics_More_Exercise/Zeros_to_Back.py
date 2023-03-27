numbers = input().split(",")

numbers = [int(i) for i in numbers]

counter = 0

for i in range(len(numbers)):
    if numbers[i] == 0:
        numbers.append(0)
        counter += 1

for i in range(len(numbers)):
    numbers.remove(0)
    counter -= 1
    if counter == 0:
        break

print(numbers)