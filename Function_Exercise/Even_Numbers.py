def even_num(str_num):
    even = []
    for el in str_num:
        if int(el) % 2 == 0:
            even.append(int(el))
    return even


numbers = input().split(" ")

print(even_num(numbers))
