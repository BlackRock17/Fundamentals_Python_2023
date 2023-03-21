integers = [int(num) for num in input().split()]
counter = int(input())

[integers.remove(min(integers)) for i in range(counter)]

print(*integers, sep=", ")

