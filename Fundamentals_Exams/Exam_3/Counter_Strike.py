energy = int(input())
won_counter = 0


while True:
    distance = input()

    if distance == "End of battle":
        print(f"Won battles: {won_counter}. Energy left: {energy}")
        break

    distance = int(distance)

    if energy < distance:
        print(f"Not enough energy! Game ends with {won_counter} won battles and {energy} energy")
        break
    else:
        energy -= distance
        won_counter += 1

    if won_counter % 3 == 0:
        energy += won_counter



