"""Using a list comprehension, write a program that receives numbers, separated by comma and space ", ", and prints all
the positive, negative, even, and odd numbers on separate lines as shown below.
Note: Zero is counted for a positive number
###################################EXAMPLES#######################################
Input: 1, -2, 0, 5, 3, 4, -100, -20, 12, 19, -33
Output:
Positive: 1, 0, 5, 3, 4, 12, 19
Negative: -2, -100, -20, -33
Even: -2, 0, 4, -100, -20, 12
Odd: 1, 5, 3, 19, -33

Input: 1, 2, 53, 2, 21
Output:
Positive: 1, 2, 53, 2, 21
Negative:
Even: 2, 2
Odd: 1, 53, 21
"""


def positive_func(numbers):
    result = [str(x) for x in numbers if x >= 0]
    return result


def negative_func(numbers):
    result = [str(x) for x in numbers if x < 0]
    return result


def even_func(numbers):
    result = [str(x) for x in numbers if x % 2 == 0]
    return result


def odd_func(numbers):
    result = [str(x) for x in numbers if x % 2 != 0]
    return result


data = [int(num) for num in input().split(", ")]

print(f"Positive: {', '.join(positive_func(data))}")
print(f"Negative: {', '.join(negative_func(data))}")
print(f"Even: {', '.join(even_func(data))}")
print(f"Odd: {', '.join(odd_func(data))}")



