text = input().split(">>")

total = 0
for car in text:
    car_type, year, km = car.split()
    year = int(year)
    km = int(km)

    if car_type == "family":
        tax = 50
        tax -= 5 * year
        tax += (km // 3000) * 12
        print(f"A {car_type} car will pay {tax:.2f} euros in taxes.")
        total += tax

    elif car_type == "heavyDuty":
        tax = 80
        tax -= 8 * year
        tax += (km // 9000) * 14
        print(f"A {car_type} car will pay {tax:.2f} euros in taxes.")
        total += tax

    elif car_type == "sports":
        tax = 100
        tax -= 9 * year
        tax += (km // 2000) * 18
        print(f"A {car_type} car will pay {tax:.2f} euros in taxes.")
        total += tax

    else:
        print("Invalid car type.")

print(f"The National Revenue Agency will collect {total:.2f} euros in taxes.")


