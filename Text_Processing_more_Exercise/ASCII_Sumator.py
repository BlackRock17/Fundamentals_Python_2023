first_char = ord(input())
second_char = ord(input())
text = input()

result = 0

for el in text:
    num = ord(el)

    if first_char < num < second_char:
        result += num
print(result)

