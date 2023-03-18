numbers = [int(x) for x in input().split()]

for index in range(len(numbers)):
    if numbers[index] > 0:
        numbers[index] = -numbers[index]
    else:
        numbers[index] = abs(numbers[index])

print(numbers)

