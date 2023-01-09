"""You will receive a single number. You should write a function that returns the sum of all even and all odd digits in a given number. The result should be returned as a single string in the format:
"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}"
Print the result of the function on the console.
###################################EXAMPLES#######################################
Input: 1000435
Output: Odd sum = 9, Even sum = 4

Input: 3495892137259234
Output: Odd sum = 54, Even sum = 22
"""


def odd_and_even_sum(number):
    even_sum = 0
    odd_sum = 0
    for current_digit in number:

        if int(current_digit) % 2 == 0:
            even_sum += int(current_digit)

        else:
            odd_sum += int(current_digit)
    return odd_sum, even_sum


user_number_str = input()
odd_sum_digits, even_sum_digits = odd_and_even_sum(user_number_str)
print(f"Odd sum = {odd_sum_digits}, Even sum = {even_sum_digits}")


def even_and_odd_numbers(number):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for digit in number:
        if int(digit) % 2 == 0:  # digit is even
            sum_of_even_digits += int(digit)
        else:  # digit is odd
            sum_of_odd_digits += int(digit)
    return sum_of_odd_digits, sum_of_even_digits


number_as_string = input()
sum_odd_digits, sum_even_digits = even_and_odd_numbers(number_as_string)
print(f"Odd sum = {sum_odd_digits}, Even sum = {sum_even_digits}")