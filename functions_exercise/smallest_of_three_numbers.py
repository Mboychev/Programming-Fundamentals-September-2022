"""Write a function that receives three integer numbers and returns the smallest.
Print the result on the console. Use an appropriate name for the function.
###################################EXAMPLES#######################################
Input:
2
5
3
Output: 2

Input:
600
342
123
Output: 123

Input:
25
21
4
Output: 4
"""

# def smallest_integer(num1, num2, num3):
#     a = min(first_number, second_number, third_number)
#     return a
#
# first_number = int(input())
# second_number = int(input())
# third_number = int(input())
#
# print(smallest_integer(first_number, second_number, third_number))

first_number = int(input())
second_number = int(input())
third_number = int(input())

result = lambda a, b, c: min(a, b, c)
print(result(first_number, second_number, third_number))