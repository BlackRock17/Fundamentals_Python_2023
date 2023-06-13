country = input().split(", ")
capital = input().split(", ")

result = {country[index]: capital[index] for index in range(len(country))}

for country, capital in result.items():
    print(f"{country} -> {capital}")


