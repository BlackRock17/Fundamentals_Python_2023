def increase_decrease(pokemons_data, pokemon_value):
    for value in range(len(pokemons_data)):
        if pokemons_data[value] <= pokemon_value:
             pokemons_data[value] += pokemon_value
        else:
            pokemons_data[value] -= pokemon_value
    return pokemons_data


pokemons = [int(i) for i in input().split()]
result = 0

while pokemons:
    index = int(input())

    if index < 0:
        remove_index = pokemons.pop(0)
        result += remove_index
        pokemons.insert(0, pokemons[-1])
        increase_decrease(pokemons, remove_index)

    elif index > len(pokemons) - 1:
        remove_index = pokemons.pop(-1)
        pokemons.append(pokemons[0])
        result += remove_index
        increase_decrease(pokemons, remove_index)

    else:
        result += pokemons[index]
        remove_index = pokemons.pop(index)
        increase_decrease(pokemons, remove_index)

print(result)


