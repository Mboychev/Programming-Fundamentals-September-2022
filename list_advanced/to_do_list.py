"""You will be receiving to-do notes until you get the command "End". The notes will be in the format:
"{importance}-{note}".
Return a list containing all to-do notes sorted by importance in ascending order.
The importance value will always be an integer between 1 and 10 (inclusive).
Hint
•	Use the pop() and insert() methods.
###################################EXAMPLES#######################################
Input:
2-Walk the dog
1-Drink coffee
6-Dinner
5-Work
End
Output: ['Drink coffee', 'Walk the dog', 'Work', 'Dinner']

Input:
3-C
2-A
1-B
6-V
End
Output: ['B', 'A', 'C', 'V']
"""

tasks = []

while True:

    command = input()

    if command == "End":
        break

    split_command = command.split("-")
    priority = int(split_command[0])
    current_tasks = split_command[1]
    tasks.append((priority, current_tasks))


sorted_tasks = [task_data[1] for task_data in sorted(tasks)]
print(sorted_tasks)
#
# command_lst = [0] * 10
#
# while True:
#
#     command = input()
#
#     if command == "End":
#         break
#
#     split_command = command.split("-")
#     priority = int(split_command[0]) - 1
#     current_command = split_command[1]
#     command_lst.pop(priority)
#     command_lst.insert(priority, current_command)
#
# print(list(x for x in command_lst if x !=0))


