"""You will receive three integer numbers.
Write functions named:
•	sum_numbers() that returns the sum of the first two integers
•	subtract() that returns the difference between the returned result of the first function and the third integer
Wrap the two functions in a function named add_and_subtract() which will receive the three numbers as parameters.
Print the result of the subtract() function on the console.
###################################EXAMPLES#######################################
Input:
23
6
10
Output: 19

Input:
1
17
30
Output: -12

Input:
42
58
100
Output: 0
"""


def sum_numbers(num1, num2):
    result = num1 + num2
    return result


def subtract(n1, n2):
    result = n1 - n2
    return result


def add_and_subtract(nu1, nu2, nu3):
    result = subtract(sum_numbers(nu1, nu2), nu3)
    return result


number_one = int(input())
number_two = int(input())
number_three = int(input())

print(add_and_subtract(number_one, number_two, number_three))