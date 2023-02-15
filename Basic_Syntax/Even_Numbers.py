n = int(input())

for i in range(n):
    next_num = int(input())
    if next_num % 2 == 1:
        print(f"{next_num} is odd!")
        break
else:
    print("All numbers are even.")