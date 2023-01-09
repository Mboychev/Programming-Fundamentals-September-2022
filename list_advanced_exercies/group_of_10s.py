"""Write a program that receives a sequence of numbers (a string containing integers separated by ", ") and prints the
numbers sorted into lists of 10's in the format "Group of {group}'s: {list_of_numbers}".
Examples:
•	The numbers 2, 8, 4, and 10 fall into the group of 10's.
•	The numbers 13, 19, 14, and 15 fall into the group of 20's.
For more clarification, see the examples below.
###################################EXAMPLES#######################################
Input: 8, 12, 38, 3, 17, 19, 25, 35, 50
Output:
Group of 10's: [8, 3]
Group of 20's: [12, 17, 19]
Group of 30's: [25]
Group of 40's: [38, 35]
Group of 50's: [50]

Input: 1, 3, 3, 4, 34, 35, 25, 21, 33
Output:
Group of 10's: [1, 3, 3, 4]
Group of 20's: []
Group of 30's: [25, 21]
Group of 40's: [34, 35, 33]
"""

data = input()
data_int = [int(x) for x in data.split(", ")]

max_value = 10
group_counter = 0

while len(data_int) > 0:

    current_group = []

    for index, value in enumerate(data_int):
        if value <= max_value:
            current_group.append(value)
            data_int.pop(index)
            data_int.insert(index, 0)

    for number in range(len(data_int)):
        if 0 in data_int:
            data_int.remove(0)
    max_value += 10
    group_counter += 10
    print(f"Group of {group_counter}'s: {current_group}")

