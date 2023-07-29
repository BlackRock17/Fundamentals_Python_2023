num_cars = int(input())

cars = {}

for _ in range(num_cars):
    info = input().split("|")
    cars[info[0]] = [int(info[1]), int(info[2])]

while True:
    info_ = input()

    if info_ == "Stop":
        break

    info_ = info_.split(" : ")
    command = info_[0]
    car = info_[1]

    if command == "Drive":
        distance = int(info_[2])
        fuel = int(info_[3])

        if cars[car][1] < fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car][0] += distance
            cars[car][1] -= fuel
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")

        if cars[car][0] >= 100000:
            del cars[car]
            print(f"Time to sell the {car}!")

    elif command == "Refuel":
        fuel = int(info_[2])
        current_fuel = cars[car][1]

        cars[car][1] = min(cars[car][1] + fuel, 75)
        print(f"{car} refueled with {cars[car][1] - current_fuel} liters")

    elif command == "Revert":
        kilometers = int(info_[2])

        if cars[car][0] - kilometers < 10000:
            cars[car][0] = 10000
        else:
            cars[car][0] -= kilometers
            print(f"{car} mileage decreased by {kilometers} kilometers")

for key, value in cars.items():
    print(f"{key} -> Mileage: {value[0]} kms, Fuel in the tank: {value[1]} lt.")


