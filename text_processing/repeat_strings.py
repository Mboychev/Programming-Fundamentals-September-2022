"""Write a program that reads a sequence of strings, separated by a single space. Each string should be repeated N
times, where N is the length of the string. Print the final strings concatenated into one string.
###################################EXAMPLES#######################################
Input: hi abc add
Output: hihiabcabcabcaddaddadd

Input: work
Output: workworkworkwork

Input: ball
Output: ballballballball
"""

sequence_of_string = input().split(" ")

for current_element in sequence_of_string:
    print(current_element * len(current_element), end="")