"""Write a program that receives strings on different lines and extracts only the numbers.
Print all extracted numbers on a single line, separated by a single space.
###################################EXAMPLES#######################################
Input:
The300
What is that?
I think it's the 3rd movie
Let's watch it at 22:45
Output: 300 3 22 45

Input:
123a456
789b987
654c321
0
Output: 123 456 789 987 654 321 0

Input:
Let's go11!!!11!
Okey!1!
Output: 11 11 1
"""

import re

data = input()

while data:

    pattern = r"\d+"

    matches = re.findall(pattern, data)
    if matches:
        print(' '.join(matches), end=" ")
    data = input()