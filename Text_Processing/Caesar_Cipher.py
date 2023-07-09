text = input()

new_text = ""

for el in text:
    new_text += chr(ord(el) + 3)

print(new_text)