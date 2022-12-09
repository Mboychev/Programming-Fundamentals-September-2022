"""Write a function that receives 3 characters. Concatenate all the characters into one string and print it on the
console.
###################################EXAMPLES#######################################
Input:
a
b
c

Output: abc

Input:
%
2
o

Output: %2o

Input:
1
5
p

Output: 15p
"""
first_character = input()
second_character = input()
third_character = input()

print(f"{first_character}{second_character}{third_character}")