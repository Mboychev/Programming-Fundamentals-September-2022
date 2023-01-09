"""You will be receiving names of students, their ID,
and a course of programming they have taken in the format "{name}:{ID}:{course}".
On the last line, you will receive a name of a course in snake case lowercase letters.
You should print only the information of the students who have taken the corresponding
course in the format: "{name} - {ID}" on separate lines.
Note: each student's ID will always be unique
###################################EXAMPLES#######################################
Input:
Peter:123:programming basics
John:5622:fundamentals
Maya:89:fundamentals
Lilly:633:fundamentals
fundamentals

Output:
John - 5622
Maya - 89
Lilly - 633

Input:
Alex:6:programming basics
Maria:7:programming basics
Kaloyan:9:advanced
Todor:10:fundamentals
programming_basics

Output:
Alex - 6
Maria - 7
"""


students = {}
data = input().split(":")

while len(data) > 1:

    name, id, course = data[0], data[1], data[2]

    if course not in students.keys():
        students[course] = []

    students[course].append(f"{name} - {id}")
    data = input().split(":")


searched_course = data[0].replace("_", " ")

print('\n'.join(students[searched_course]))