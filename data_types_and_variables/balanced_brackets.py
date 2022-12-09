"""On the first line, you will receive n – the number of lines, which will follow. On the following n lines, you will receive one of the following:
•	Opening bracket – "(",
•	Closing bracket – ")" or
•	Random string
Your task is to find out if the brackets are balanced. That means after every opening bracket should follow a
closing one. Nested parentheses are not valid, and if, for example, two consecutive opening brackets exist,
the expression should be marked as unbalanced. You should print "BALANCED" if the parentheses
are balanced and "UNBALANCED" otherwise.

###################################EXAMPLES#######################################
Input:
8
(
5 + 10
)
* 2 +
(
5
)
-12

Output: BALANCED

Input:
6
12 *
)
10 + 2 -
(
5 + 10
)

Output: UNBALANCED
"""

number_of_lines = int(input())
opening_counter = 0
closed_counter = 0

for i in range(number_of_lines):

    character_input = input()

    if character_input == "(":
        opening_counter += 1

    elif character_input == ")":
        closed_counter += 1

    diff = abs(opening_counter - closed_counter)

    if diff > 1:
        break
    if closed_counter > opening_counter:
        break

if opening_counter == closed_counter:
    print("BALANCED")
else:
    print("UNBALANCED")


