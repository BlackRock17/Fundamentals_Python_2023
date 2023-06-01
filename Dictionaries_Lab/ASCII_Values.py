characters = input().split(", ")

char_value = {char: ord(char) for char in characters}

print(char_value)