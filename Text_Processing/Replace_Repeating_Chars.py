text = input()

new_text = ""

for index in range(len(text)):
    if index + 1 == len(text):
        new_text += text[index]
        break

    if text[index] == text[index+1]:
        continue
    else:
        new_text += text[index]

print(new_text)
