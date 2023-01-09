"""Write a program that receives info from the console about people and their phone numbers.
Each entry should have a name and a number (both strings) separated by a "-". If you receive a name that already exists
in the phonebook, update its number.
After filling the phonebook, you will receive a number – N. Your program should be able to perform a search of contact
by name and print its details in the format: "{name} -> {number}".
In case the contact isn't found, print: "Contact {name} does not exist."

###################################EXAMPLES#######################################
Input:
Adam-0888080808
2
Mery
Adam
Output:
Contact Mery does not exist.
Adam -> 0888080808

Input:
Adam-+359888001122
Ralf-666
George-5559393
Silvester-02/987665544
4
Silvester
silvester
Rolf
Ralf
Output:
Silvester -> 02/987665544
Contact silvester does not exist.
Contact Rolf does not exist.
Ralf -> 666
"""

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








