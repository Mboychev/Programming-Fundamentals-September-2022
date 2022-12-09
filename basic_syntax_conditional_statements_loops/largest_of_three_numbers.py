"""Write a program that receives three whole numbers and prints the largest one.

Input:
3
-1
5

Output:
5

Input:
0
-1
-2

Output:
0
"""

first_number = int(input())
second_number = int(input())
third_number = int(input())

max_number = max(first_number, second_number, third_number)

print(max_number)

# first_number, second_number, third_number = int(input()), int(input()), int(input())
# print(max(first_number, second_number, third_number))