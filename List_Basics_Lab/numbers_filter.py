n = int(input())

even = []
odd = []
negative = []
positive = []

for i in range(n):
    number = int(input())

    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

    if number < 0:
        negative.append(number)
    else:
        positive.append(number)

command = input()

if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "negative":
    print(negative)
else:
    print(positive)
