strings = input().split()

total = 0

short_word = min(strings, key=len)

for char in range(len(short_word)):
    total += ord(strings[0][char]) * ord(strings[1][char])

long_word = max(strings, key=len)

if len(long_word) > len(short_word):
    for index in range(len(short_word), len(long_word)):
        total += ord(long_word[index])

print(total)


