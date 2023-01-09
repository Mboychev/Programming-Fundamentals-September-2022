"""Write a program that receives a single string (integers separated by a comma and space ", "), finds all the zeros,
and moves them to the back without messing up the other elements. Print the resulting integer list.
###################################EXAMPLES#######################################
Input: 1, 0, 1, 2, 0, 1, 3
Output: [1, 1, 2, 1, 3, 0, 0]

Input: 0, 5, 0, 4, 0, 0, 5
Output: [5, 4, 5, 0, 0, 0, 0]"""

single_string_list = input().split(", ")
int_lst = []
zero_counter = 0

for number in single_string_list:
    number = int(number)
    int_lst.append(number)

for current_number in int_lst:
    if current_number == 0:
        int_lst.remove(current_number)
        int_lst.append(0)

print(int_lst)