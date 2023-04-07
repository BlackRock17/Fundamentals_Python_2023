import math

def factorial(num):
    sum = math.factorial(num)
    return sum

def divide(a, b):
    return a / b

num_1 = int(input())
num_2 = int(input())

print(f"{divide(factorial(num_1), factorial(num_2)):.2f}")

#### SECOND

import math

num_1 = math.factorial(int(input()))
num_2 = math.factorial(int(input()))

print(f"{num_1 / num_2:.2f}")


