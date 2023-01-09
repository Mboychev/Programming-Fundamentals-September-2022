"""Write a program that reads a single string with numbers separated by comma and space ", ".
Print the indices of all even numbers.
###################################EXAMPLES#######################################
Input: 3, 2, 1, 5, 8
Output: [1, 4]

Input: 2, 4, 6, 9, 10
Output: [0, 1, 2, 4]
"""

numbers = list(map(int, input().split(", ")))

found_indexes_or_no = map(lambda x: x if numbers[x] % 2 == 0 else "No", numbers)
even_indexes = list(filter(lambda a: a != "No", found_indexes_or_no))
print(even_indexes)