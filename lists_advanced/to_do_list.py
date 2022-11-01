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
#
#
#
#
#
#
#
#


