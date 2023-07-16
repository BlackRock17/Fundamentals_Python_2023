import re

n = int(input())
regex_name = r"(?<=@)[A-Za-z]+"
regex_age = r"(?<=#)\d+"

for _ in range(n):
    text = input()

    name = re.findall(regex_name, text)
    age = re.findall(regex_age, text)

    print(f"{name[0]} is {age[0]} years old.")






