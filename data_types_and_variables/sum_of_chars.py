"""Write a program, which sums the ASCII codes of N characters and prints the sum on the console. On the first line, you will receive N – the number of lines. On the following N lines – you will receive a letter per line. Print the total sum in the following format: "The sum equals: {total_sum}".
Note: n will be in the interval [1…20].
###################################EXAMPLES#######################################
Input:
5
A
b
C
d
E

Output: The sum equals: 399

Input:
12
S
o
f
t
U
n
i
R
u
l
z
z

Output: The sum equals: 1263
"""

total_numbers = int(input())
total_sum = 0

for number in range(total_numbers):

    character = input()

    character_in_num = ord(character)
    total_sum += character_in_num

print(f"The sum equals: {total_sum}")
