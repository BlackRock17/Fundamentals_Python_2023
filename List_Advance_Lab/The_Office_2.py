employees = input().split()
happy_factor = int(input())

employees = list(map(lambda x: int(x) * happy_factor, employees))

filtered = list(filter(lambda x: x >= (sum(employees) / len(employees)), employees))


print(employees)
print(filtered)