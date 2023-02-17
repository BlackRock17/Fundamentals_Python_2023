budget = int(input())

while True:
    command = input()

    if command == "End":
        print("You bought everything needed.")
        break

    product = int(command)

    if product > budget:
        print("You went in overdraft!")
        break

    budget -= product

