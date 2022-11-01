# year = int(input())
# year_is_happy = False
#
# counter = 0
# counter_digits = 0
# while not year_is_happy:
#     year += 1
#
#     year_as_string = str(year)
#
#     for digit in year_as_string:
#         new_year = (year_as_string[(counter + 1):])
#
#         if digit in new_year:
#             counter = 0
#             break
#         else:
#
#             counter_digits += 1
#         counter += 1
#
#     if counter_digits == len(year_as_string):
#         year_is_happy = True
#         break
#     else:
#
#         counter_digits = 0
#
# print(year)


year = int(input())
year_is_happy = False
counter_digits = 0
counter_digits_in_year = 0
while not year_is_happy:

    year += 1
    year_in_string = str(year)

    for digit in year_in_string:

        new_year = year_in_string[counter_digits + 1:]

        if digit in new_year:
            counter_digits = 0
            break

        else:
            counter_digits += 1

        counter_digits_in_year += 1

    if counter_digits_in_year == len(year_in_string):

        year_is_happy = True
        break

    else:
        counter_digits_in_year = 0
print(year)
