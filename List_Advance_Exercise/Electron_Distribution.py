electrons = int(input())

list_of_electrons = []
counter = 1

while electrons > 0:

    electron = 2 * (counter**2)

    if electron <= electrons:
        list_of_electrons.append(electron)
        electrons -= electron
        counter += 1
    else:
        list_of_electrons.append(electrons)
        electrons = 0

print(list_of_electrons)
