deck = input().split()
shuffle = int(input())

for i in range(shuffle):
    result = []
    half = int(len(deck) / 2)
    first_half = deck[:half]
    second_half = deck[half::]

    for index in range(half):
        result.append(first_half[index])
        result.append(second_half[index])
    deck = result

print(deck)

