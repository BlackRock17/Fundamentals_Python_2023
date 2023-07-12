text = input().split()

summ = []

for word in text:
    first_num = 0
    last_num = 0
    num = int(word[1:-1])
    total = 0

    if word[0].islower():
        first_num = ord(word[0]) - 96
        total += first_num * num
    else:
        first_num = ord(word[0]) - 64
        total += num / first_num

    if word[-1].islower():
        last_num = ord(word[-1]) - 96
        total += last_num
    else:
        last_num = ord(word[-1]) - 64
        total -= last_num

    summ.append(total)

print(f"{sum(summ):.2f}")


