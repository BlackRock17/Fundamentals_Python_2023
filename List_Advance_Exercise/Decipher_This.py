secret_message = input().split()

for word in secret_message:
    nums = ""
    for el in word:
        if el.isdigit():
            nums += el

    first_letter = chr(int(nums))
    current_word = first_letter + word[len(nums):]
    current_word = list(current_word)
    current_word[1], current_word[-1] = current_word[-1], current_word[1]

    print(f"{''.join(current_word)}", end=" ")

### SECOND

secret_message = input().split()

message = ""

for word in secret_message:
    num = ""
    current_word = ""
    for el in word:
        if el.isdigit():
            num += el
    current_word += chr(int(num))
    current_word += word[len(num)::]
    current_word = list(current_word)
    current_word[1], current_word[-1] = current_word[-1], current_word[1]
    message += "".join(current_word) + " "

print(message)