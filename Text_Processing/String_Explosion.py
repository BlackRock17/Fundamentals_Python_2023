text = [el for el in input()]

counter = 0
new_text = ""

for index, el in enumerate(text):
    if el == ">":
        counter += int(text[index+1])

    if counter > 0 and el != ">":
        counter -= 1
    else:
        new_text += el
print(new_text)


