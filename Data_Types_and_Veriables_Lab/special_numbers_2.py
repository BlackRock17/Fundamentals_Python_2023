n = int(input())

for num in range(1, n + 1):
    str_of_num = str(num)
    sum = 0

    for str_num in str_of_num:
        sum += int(str_num)

    if sum == 5 or sum == 7 or sum == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")
