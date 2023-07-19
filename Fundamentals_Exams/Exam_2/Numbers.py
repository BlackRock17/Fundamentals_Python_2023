integers = [int(i) for i in input().split()]
output = []
average = round(sum(integers) / len(integers), 2)

for el in integers:
    if el > average:
        output.append(el)

output = sorted(output, reverse=True)

if not output:
    print("No")
else:
    if len(output) > 5:
        for i in range(5):
            print(output[i], end=" ")
    else:
        print(*output, sep=" ")
