def smallest_number(a, b, c):
    smallest = min(a, b, c)
    return smallest

num1 = int(input())
num2 = int(input())
num3 = int(input())

result = smallest_number(num1, num2, num3)

print(result)