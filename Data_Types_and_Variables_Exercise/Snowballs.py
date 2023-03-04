n = int(input())

value = 0
weight = 0
time = 0
quality = 0


for _ in range(n):
    weight_crt = int(input())
    time_crt = int(input())
    quality_crt = int(input())

    current_value = (weight_crt / time_crt) ** quality_crt

    if current_value > value:
        value = int(current_value)
        weight = weight_crt
        time = time_crt
        quality = quality_crt

print(f"{weight} : {time} = {value} ({quality})")
