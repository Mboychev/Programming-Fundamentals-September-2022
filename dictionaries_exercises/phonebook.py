person_and_number = input()
dict = {}

while "-" in person_and_number:

    current_name, current_number = person_and_number.split("-")
    if current_name not in dict:
        dict[current_name] = 0
    dict[current_name] = current_number
    person_and_number = input()

searched_contacts_count = int(person_and_number)

for search in range(searched_contacts_count):
    searched_name = input()

    if searched_name in dict.keys():
         print(f"{searched_name} -> {dict[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")








