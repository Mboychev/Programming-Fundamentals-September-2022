"""You are saying goodbye to your best friend: "See you next happy year". Happy Year is the year with only distinct
digits, for example, 2018. Write a program that receives an integer number and finds the next happy year.
###################################EXAMPLES#######################################
Input: 8989
Output: 9012

Input: 1001
Output: 1023
"""

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
