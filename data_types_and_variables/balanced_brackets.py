number_of_lines = int(input())
opening_counter = 0
closed_counter = 0


for i in range(number_of_lines):

    character_input = input()


    if character_input == "(":
        opening_counter += 1

    elif character_input == ")":
        closed_counter += 1

    diff = abs(opening_counter - closed_counter)

    if diff > 1:
        break
    if closed_counter > opening_counter:
        break

if opening_counter == closed_counter:

    print("BALANCED")
else:
    print("UNBALANCED")


