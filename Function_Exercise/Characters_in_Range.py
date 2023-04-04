def string(char1, char2):
    text = []
    char1 = ord(char1)
    char2 = ord(char2)
    for index in range(char1 + 1, char2):
        text.append(chr(index))
    return text


simbol_1 = input()
simbol_2 = input()

print(" ".join(string(simbol_1, simbol_2)))

