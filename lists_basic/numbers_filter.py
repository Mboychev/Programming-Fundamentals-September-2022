"""On the first line, you will receive a single number n. On the following n lines, you will receive integers. After that, you will be given one of the following commands:
•	even
•	odd
•	negative
•	positive
Filter all the numbers that fit in the category (0 counts as a positive and even). Finally, print the result.
###################################EXAMPLES#######################################
Input:
5
33
19
-2
18
998
even

Output: [-2, 18, 998]

Count of positives:
3
111
-4
0
negative

Sum of negatives: [-4]
"""

number_of_lines = int(input())
COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_NEGATIVE = "negative"
COMMAND_POSITIVE = "positive"

numbers = []

for i in range(number_of_lines):

    current_number = int(input())
    numbers.append(current_number)

command = input()
filtered_numbers = []
filtered_passes = []

for i in numbers:

    filtered_passes = (
        (command == COMMAND_EVEN and i % 2 == 0)
        or (command == COMMAND_ODD and i % 2 != 0)
        or (command == COMMAND_POSITIVE and i >= 0)
        or (command == COMMAND_NEGATIVE and i < 0))

    if filtered_passes:
        filtered_numbers.append(i)

print(filtered_numbers)



