# Using a dictionary comprehension, write a program that receives country names on the first line,
# separated by comma and space ", ", and their corresponding capital cities on the second line
# (again separated by comma and space ", "). Print each country with their capital on a separate
# line in the following format: "{country} -> {capital}".

country_names = input().split(", ")
capital_names = input().split(", ")


# dictionary = {country_names[x]: capital_names[x] for x in range(len(country_names))}

dictionary = dict(zip(country_names, capital_names))

for key, value in dictionary.items():
    print(f"{key} -> {value}")

