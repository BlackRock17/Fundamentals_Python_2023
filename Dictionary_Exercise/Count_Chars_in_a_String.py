characters = "".join(input().split(" "))
result = {}

for char in characters:
    if char not in result:
        result[char] = 0
    result[char] += 1

for char, count in result.items():
    print(f"{char} -> {count}")
