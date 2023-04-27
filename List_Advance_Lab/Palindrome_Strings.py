words = input().split()
palindrome = input()

counter = 0

pwords = [word for word in words if word == word[::-1]]

for word in pwords:
    if palindrome == word:
        counter += 1

print(pwords)
print(f"Found palindrome {counter} times")

