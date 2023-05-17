text = input()

number = ""
for el in text:
    if el.isdigit():
        number += el

new_text = ""
for el in text:
    if not el.isdigit():
        new_text += el

message = ""
index_counter = 0

for index, num in enumerate(number):
    if index % 2 == 0:
        message += new_text[index_counter:index_counter + int(num)]
    index_counter += int(num)

print(message)






