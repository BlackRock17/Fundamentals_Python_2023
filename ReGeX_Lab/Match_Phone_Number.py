import re

text = input()

matches = re.finditer(r"\+359([ -])2\1\d{3}\1\d{4}\b", text)

output = [match.group() for match in matches]

print(*output, sep=", ")