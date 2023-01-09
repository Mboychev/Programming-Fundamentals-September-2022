"""Write a program that receives a sequence of numbers (integers) separated by a single space.
It should print a list of only the even numbers. Use filter().
###################################EXAMPLES#######################################
Input: 1 2 3 4
Output: [2, 4]

Input: 1 2 3 -1 -2 -3
Output: [2, -2]
"""


def numbers_as_int(some_list):
    list_of_numbers = []
    for element in some_list:
        element_as_int = int(element)
        list_of_numbers.append(element_as_int)
    return list_of_numbers


def check_even(num):
    if num % 2 == 0:
        return True
    return False


numbers = input().split()
filtered_numbers = list(filter(check_even, numbers_as_int(numbers)))
print(filtered_numbers)