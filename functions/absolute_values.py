"""Write a program that receives a sequence of numbers, separated by a single space,
and prints their absolute value as a list. Use abs().
###################################EXAMPLES#######################################
Input: 1 2.5 -3 -4.5
Output: [1.0, 2.5, 3.0, 4.5]

Input: -0 1 10 -6.66
Output: [0.0, 1.0, 10.0, 6.66]"""

sequence = input().split(" ")
final_result = []

for current_number in sequence:
    final_result.append(abs(float(current_number)))
print(final_result)