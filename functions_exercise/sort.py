"""Write a program that receives a sequence of numbers (integers) separated by a single space.
It should print a sorted list of numbers in ascending order. Use sorted().
###################################EXAMPLES#######################################
Input: 6 2 4
Output: [2, 4, 6]

Input: 12 52 11 53 2 8 45
Output: [2, 8, 11, 12, 45, 52, 53]
"""
result = list(sorted(map(lambda x: int(x), input().split(" "))))
print(result)
