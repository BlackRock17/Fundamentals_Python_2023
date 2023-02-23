word_1 = input()
word_2 = input()

save_str = ""
priv_str = word_1

for i in range(len(word_1)):
    for j in range(i + 1):
        save_str += word_2[j]
    for k in range(i + 1, len(word_1)):
        save_str += word_1[k]

    if not save_str == priv_str:
        print(save_str)
    priv_str = save_str
    save_str = ""

# second solution

str1 = input()
str2 = input()

privios_str = str1

for index in range(len(str1) + 1):
    new_str = ""
    new_str += str2[:index]
    new_str += str1[index::]

    if new_str != privios_str:
        print(new_str)
    privios_str = new_str
