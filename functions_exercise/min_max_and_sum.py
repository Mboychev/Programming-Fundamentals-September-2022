"""Write a program that receives a sequence of numbers (integers) separated by a single space. It should print the min and max values of the given numbers and the sum of all the numbers in the list. Use min(), max() and sum().
The output should be as follows:
•	On the first line: "The minimum number is {minimum number}"
•	On the second line: "The maximum number is {maximum number}"
•	On the third line: "The sum number is: {sum of all numbers}"
###################################EXAMPLES#######################################
Input: 2 4 6
Output:
The minimum number is 2
The maximum number is 6
The sum number is: 12

Input: 12 52 11 53 2 8 45
Output:
The minimum number is 2
The maximum number is 53
The sum number is: 183
"""


def min_max_sum(numbers):

    result = list(map(lambda x: int(x), numbers.split(" ")))
    min_number = min(result)
    max_number = max(result)
    total_number_sum = sum(result)

    return min_number, max_number, total_number_sum


sequence_of_numbers = input()
minimal, maximal, the_sum = min_max_sum(sequence_of_numbers)
print(f"The minimum number is {minimal}")
print(f"The maximum number is {maximal}")
print(f"The sum number is: {the_sum}")
