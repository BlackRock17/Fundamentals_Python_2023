def odd_even_sum(str_num):
    odd_sum = 0
    even_sum = 0
    for el in str_num:
        if int(el) % 2 == 1:
            odd_sum += int(el)
        else:
            even_sum += int(el)
    return [odd_sum, even_sum]

number = input()
result = odd_even_sum(number)

print(f"Odd sum = {result[0]}, Even sum = {result[1]}")

