"""Write a program that receives a list of characters separated by ", ".
It should create a dictionary with each character as a key and its ASCII value as a value.
Try solving that problem using comprehension
###################################EXAMPLES#######################################

Input: a, b, c, a
Output: {'a': 97, 'b': 98, 'c': 99}

Input: d, c, m, h
Output: {'d': 100, 'c': 99, 'm': 109, 'h': 104}
"""

list_of_chars = {key: ord(key) for key in input().split(", ")}
print(list_of_chars)