population = [int(num) for num in input().split(", ")]
min_wealth = int(input())

distribution = True

for index1, wealthiest in reversed(list(enumerate(population))):
    for index, poorest in enumerate(population):
        if poorest < min_wealth and wealthiest - min_wealth >= min_wealth - poorest:
            population[index] = min_wealth
            population[index1] -= min_wealth - poorest
            wealthiest -= min_wealth - poorest

for el in population:
    if el < min_wealth:
        distribution = False

if distribution:
    print(population)
else:
    print("No equal distribution possible")
