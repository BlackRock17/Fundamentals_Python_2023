def tribonacci(n):
    list = [0, 0, 1]
    for i in range(n - 1):
        current_sum = list[-1] + list[-2] + list[-3]
        list.append(current_sum)
    return list


n = int(input())

result = tribonacci(n)
result.remove(0)
result.remove(0)
result_string = map(str, result)

print(" ".join(result_string))
