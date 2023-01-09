"""A palindrome is a number that reads the same backward as forward, such as 323 or 1001.
Write a function that receives a list of positive integers, separated by comma and space ", ".
The function should check if each integer is a palindrome - True or False. Print the result.
###################################EXAMPLES#######################################
Input: 123, 323, 421, 121
Output:
False
True
False
True

Input: 32, 2, 232, 1010
Output:
False
True
True
False
"""


def palindrome_check(number):

    for current_number in number:
        turned_number = current_number[::-1]
        if turned_number == current_number:
            print(True)
        else:
            print(False)


list_of_numbers = input().split(", ")
palindrome_check(list_of_numbers)