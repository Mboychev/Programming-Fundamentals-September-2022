"""Write a program to check if a number is prime. A prime number is a natural number greater than 1, not a product of
two smaller natural numbers. For example, the only ways of writing 5 as a product, 1 × 5 or 5 × 1, involve 5 itself.
The input comes as an integer number.
The output should be True if the number is prime and False otherwise.
###################################EXAMPLES#######################################
Input: 7
Output: True

Input: 8
Output: False

Input: 81
Output: False
"""

num = int(input())

counter = 0

for numbers in range(num, 0, -1):
    for digits in range(num, 0, -1):
        result = int(digits * numbers)
        if result == num and result % num == 0:
            counter += 1

if counter == 2:
    print("True")
else:
    print("False")
