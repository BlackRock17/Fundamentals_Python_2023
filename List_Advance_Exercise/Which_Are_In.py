substrings = input().split(", ")
words = input().split(", ")

subs_list = [subs for subs in substrings for word in words if subs in word]

print(sorted(set(subs_list), key=subs_list.index))

#### SECOND

subs = input().split(", ")
words = input().split(", ")

output = []

for el in subs:
    found = False
    for word in words:
        if el in word:
            output.append(el)
            found = True
        if found:
            break

print(output)


