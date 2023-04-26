numbers = list(map(int, input().split(", ")))

#num_index = []
#for index, num in enumerate(numbers):
#    if num % 2 == 0:
#        num_index.append(index)

#print(num_index)

index = [index for index in range(len(numbers)) if numbers[index] % 2 == 0]

print(index)