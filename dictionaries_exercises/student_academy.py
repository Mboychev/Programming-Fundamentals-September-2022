"""Write a program that keeps the information about students and their grades.
On the first line, you will receive an integer number representing the next pair of rows. On the next lines,
you will be receiving each student's name and their grade.
Keep track of all grades for each student and keep only the students with an average grade higher
than or equal to 4.50.
Print the final dictionary with students and their average grade in the following format:
"{name} -> {averageGrade}"
Format the average grade to the 2nd decimal place.
###################################EXAMPLES#######################################
Input:
5
John
5.5
John
4.5
Alice
6
Alice
3
George
5
Output:
John -> 5.00
Alice -> 4.50
George -> 5.00

Input:
5
Amanda
3.5
Amanda
4
Rob
5.5
Christian
5
Robert
6
Output:
Rob -> 5.50
Christian -> 5.00
Robert -> 6.00
"""


pairs = int(input())
dict = {}
data_lst = []


for index in range(pairs * 2):
    student_data = input()
    data_lst.append(student_data)

for current_index in range(0, len(data_lst), 2):

    if data_lst[current_index] not in dict.keys():
        dict[data_lst[current_index]] = []
    dict[data_lst[current_index]].append(float(data_lst[current_index + 1]))


for indx, value in dict.items():
    average_grade = sum(value)/len(dict[indx])
    if average_grade >= 4.5:
        print(f"{indx} -> {average_grade:.2f}")

