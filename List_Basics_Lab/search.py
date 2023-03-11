n = int(input())
word = input()

text = []
filtred_text = []

for i in range(n):
    current_text = input()
    text.append(current_text)

    if word in current_text:
        filtred_text.append(current_text)

print(text)
print(filtred_text)

