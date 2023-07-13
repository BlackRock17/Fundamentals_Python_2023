text = input()

symbol = ""
current_text = ""

for index, el in enumerate(text):
    if not el.isdigit():
        current_text += el.upper()

    if index < len(text) - 1:
        if text[index].isdigit() and text[index+1].isdigit():
            num = el + text[index+1]
            num = int(num)
            symbol += current_text * num
            current_text = ""

    if el.isdigit():
        num = int(el)
        symbol += current_text * num
        current_text = ""

num_symbols = set(symbol)

print(f"Unique symbols used: {len(num_symbols)}")
print(symbol)
