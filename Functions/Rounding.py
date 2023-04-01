numbers = [float(x) for x in input().split()]

result = []

for i in range(len(numbers)):
    result.append(round(numbers[i]))

print(result)
