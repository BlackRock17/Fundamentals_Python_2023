def convert(text, command):
    result = []
    if text == "int":
        result.append(int(command) * 2)
    elif text == "real":
        result.append(float(command) * 1.5)
    else:
        result.append(command)
    return result

text = input()
command = input()

result = convert(text, command)

if text == "int":
    print(result[0])
elif text == "real":
    print(f"{result[0]:.2f}")
elif text == "string":
    print(f"${result[0]}$")



