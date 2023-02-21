budget = float(input())
prc_flour = float(input())
prc_eggs = prc_flour * 0.75
prc_milk = (prc_flour * 1.25) / 4

prc_bread = prc_milk + prc_eggs + prc_flour

easter_braed = 0
eggs = 0

while budget >= prc_bread:
    budget -= prc_bread
    easter_braed += 1
    eggs += 3

    if easter_braed % 3 == 0:
        eggs -= easter_braed - 2

print(f"You made {easter_braed} loaves of Easter bread! Now you have {eggs} eggs and {budget:.2f}BGN left.")