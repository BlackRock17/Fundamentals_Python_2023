import math

def distance(a, b):
    pair = abs(a) + abs(b)
    return pair

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
a1 = float(input())
b1 = float(input())
a2 = float(input())
b2 = float(input())

xy1 = distance(x1, y1)
xy2 = distance(x2, y2)
ab1 = distance(a1, b1)
ab2 = distance(a2, b2)

if xy1 + xy2 >= ab1 + ab2:
    if xy1 <= xy2:
        print(f"({math.floor(x1)}, {math.floor(y1)})({math.floor(x2)}, {math.floor(y2)})")
    else:
        print(f"({math.floor(x2)}, {math.floor(y2)})({math.floor(x1)}, {math.floor(y1)})")
else:
    if ab1 <= ab2:
        print(f"({math.floor(a1)}, {math.floor(b1)})({math.floor(a2)}, {math.floor(b2)})")
    else:
        print(f"({math.floor(a2)}, {math.floor(b2)})({math.floor(a1)}, {math.floor(b1)})")








