numbers = input().split(", ")

for num in numbers:
    palindrome = False
    if num == num[::-1]:
        palindrome = True
    print(palindrome)
