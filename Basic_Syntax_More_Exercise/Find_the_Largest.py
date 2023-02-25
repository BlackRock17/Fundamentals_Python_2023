number = input()

for i in range(9, -1, -1):
    for j in number:
        if int(j) == int(i):
            print(i, end="")
