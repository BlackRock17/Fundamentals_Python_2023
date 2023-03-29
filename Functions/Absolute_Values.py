numbers = input().split()

list_num = []

for num in numbers:
    num = float(num)
    list_num.append(abs(num))

print(list_num)
