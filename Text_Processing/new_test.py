import re

text = input()

result = re.split(r"\s+[,]\s+", text)

print(result)