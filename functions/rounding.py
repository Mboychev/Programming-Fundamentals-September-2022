"""Write a program that rounds all the given numbers, separated by a single space, and prints the result as a list.
Use round().
###################################EXAMPLES#######################################
Input: 1.0 2.5 3.0 4.5
Output: [1, 2, 3, 4]

Input: 2.56 1.9 -3.4 8.1
Output: [3, 2, -3, 8]"""


def rounding(b):

    a = b.split(" ")
    b = []
    for current_number in a:
        a = float(current_number)
        b.append(round(a))
    return b


numbers = input()
print(rounding(numbers))