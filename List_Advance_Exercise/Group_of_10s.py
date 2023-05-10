numbers = [int(num) for num in input().split(", ")]

counter = 10

while numbers:

    current_group = []

    for num in numbers:
        if num <= counter:
            current_group.append(num)

    for num in current_group:
        numbers.remove(num)

    print(f"Group of {counter}'s: {current_group}")
    counter += 10


##### SECOND with DICTIONARY

import math

numbers = [int(i) for i in input().split(", ")]

result = {}

for num_group in range(10, math.ceil(max(numbers) / 10) * 10 + 10, 10):
    result[num_group] = []
    for el in numbers:
        if el <= num_group and el > num_group - 10:
            result[num_group].append(el)
    print(f"Group of {num_group}'s: {result[num_group]}")


