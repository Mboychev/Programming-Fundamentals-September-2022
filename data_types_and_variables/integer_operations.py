"""Write a program that reads four integer numbers. It should add the first to the second number, integer divide the
sum by the third number, and multiply the result by the fourth number. Print the final result.
###################################EXAMPLES#######################################
Input:
10
20
3
3

Output: 30

Input:
15
14
2
3

Output: 42
"""

first_number = int(input())
second_number = int(input())
third_number = int(input())
fourth_number = int(input())

first_sum = first_number + second_number
division = int(first_sum/third_number)
result = division * fourth_number

print(result)