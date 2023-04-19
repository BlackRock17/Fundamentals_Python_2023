def perfect_num(num):
    is_perfect = True
    sum_num = 0
    for div in range(1, int(num / 2) + 1):
        if num % div == 0:
            sum_num += div
    if not sum_num == num:
        is_perfect = False
    return is_perfect


number = int(input())

if perfect_num(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
