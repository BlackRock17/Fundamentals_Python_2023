def operation(a, b, operator):
    if operator == "multiply":
        return a * b
    elif operator == "divide":
        return a // b
    elif operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b



operator = input()
num_1 = int(input())
num_2 = int(input())

print(operation(num_1, num_2, operator))
