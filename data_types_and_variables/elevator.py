"""Calculate how many courses will be needed to elevate N persons by using an elevator with a capacity of P persons.
The input holds two lines: the number of people N and the capacity P of the elevator.
###################################EXAMPLES#######################################
Input:
17
3

Output: 6

Input:
4
5

Output: 1

Input:
10
5

Output: 2
"""

from math import ceil

capacity_of_elevator = int(input())
number_of_people = int(input())

courses = capacity_of_elevator / number_of_people

print(ceil(courses))





