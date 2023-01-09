"""Write a program that keeps the information about companies and their employees.
You will be receiving company names and an employees' id until you receive the command "End" command.
Add each employee to the given company. Keep in mind that a company cannot have two employees with the same id.
Print the company name and each employee's id in the following format:
"{company_name}
-- {id1}
-- {id2}
…
-- {idN}"
Input / Constraints
•	Until you receive the "End" command, you will be receiving input in the format:
"{company_name} -> {employee_id}".
•	The input always will be valid.
###################################EXAMPLES#######################################
Input:
SoftUni -> AA12345
SoftUni -> BB12345
Microsoft -> CC12345
HP -> BB12345
End
Output:
SoftUni
-- AA12345
-- BB12345
Microsoft
-- CC12345
HP
-- BB12345


Input:
SoftUni -> AA12345
SoftUni -> CC12344
Lenovo -> XX23456
SoftUni -> AA12345
Movement -> DD11111
End
Output:
SoftUni
-- AA12345
-- CC12344
Lenovo
-- XX23456
Movement
-- DD11111
"""

dict = {}

while True:

    data = input()

    if data == "End":
        break

    name, id = data.split(" -> ")

    if name not in dict.keys():
        dict[name] = []

    if id not in dict[name]:
        dict[name].append(id)

for user_name in dict.keys():
    print(user_name)
    for value in dict[user_name]:
        print(f"-- {value}")