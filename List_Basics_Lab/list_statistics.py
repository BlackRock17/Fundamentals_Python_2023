n = int(input())

positives = []
negaives = []

for _ in range(n):
    number = int(input())

    if number >= 0:
        positives.append(number)
    else:
        negaives.append(number)

print(positives)
print(negaives)
print(f"Count of positives: {len(positives)}")
print(f"Sum of negatives: {sum(negaives)}")




