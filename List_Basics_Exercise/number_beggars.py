money_for_beggars = [int(x) for x in input().split(", ")]
beggars = int(input())
counter = 0
reslut = []

for beggar in range(beggars):
    reslut.append(0)
    for sum in range(counter, len(money_for_beggars), beggars):
        reslut[beggar] += money_for_beggars[sum]
    counter += 1

print(reslut)


#   SECOND   SOLUTION

#amount = input().split(",")
#amount = list(map(int, amount))
#beggars = int(input())

#total_for_each_beggar = []

#for beggar in range(beggars):
#    current_sum = 0

#    for sum in range(beggar, len(amount), beggars):
#        current_sum += int(amount[sum])

#    total_for_each_beggar.append(current_sum)

#print(total_for_each_beggar)