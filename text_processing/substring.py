"""On the first line, you will receive a string. On the second line, you will receive a second string.
Write a program that removes all the occurrences of the first string in the second until there is no match.
At the end, print the remaining string.
###################################EXAMPLES#######################################
Input:
ice
kicegiciceeb

Output: kgb
"""

first_str = input()
second_str = input()

while first_str in second_str:
    second_str = second_str.replace(first_str, "")
print(second_str)
