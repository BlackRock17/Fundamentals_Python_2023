import math

def check_point(a, b):
    total = abs(a) + abs(b)
    return total

x1 = math.floor(float(input()))
y1 = math.floor(float(input()))
x2 = math.floor(float(input()))
y2 = math.floor(float(input()))

if check_point(x1, y1) > check_point(x2, y2):
    print(f"({int(x2)}, {int(y2)})")
else:
    print(f"({int(x1)}, {int(y1)})")
