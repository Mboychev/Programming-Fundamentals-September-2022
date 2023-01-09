"""On the first line, you will receive a single number n. On the following n lines,
you will receive names of courses. You should create a list of courses and print it.
###################################EXAMPLES#######################################
Input:
2
PB Python
PF Python

Output: ['PB Python', 'PF Python']

Input:
4
Front-End
C# Web
JS Core
Programming Fundamentals

Output: ['Front-End', 'C# Web', 'JS Core', 'Programming Fundamentals']
"""

number_of_lines = int(input())
courses = []

for i in range(number_of_lines):

    courses_name = input()
    courses.append(courses_name)

print(courses)