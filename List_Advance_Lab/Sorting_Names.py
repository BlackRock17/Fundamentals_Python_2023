names = input().split(", ")

names = sorted(names, key=len, reverse=True)


print(names)

