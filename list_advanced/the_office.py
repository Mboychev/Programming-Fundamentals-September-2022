"""You will receive two lines of input:
•	a list of employees' happiness as a string of numbers separated by a single space
•	a happiness improvement factor (single number).
Your task is to find out if the employees are generally happy in their office.
First, multiply each employee's happiness by the factor.
Then, print one of the following lines:
•	If half or more of the employees have happiness greater than or equal to the average:
"Score: {happy_count}/{total_count}. Employees are happy!"
•	Otherwise:
"Score: {happy_count}/{total_count}. Employees are not happy!"
###################################EXAMPLES#######################################
Input:
1 2 3 4 2 1
3
Output: Score: 2/6. Employees are not happy!

Input:
2 3 2 1 3 3
4
Output: Score: 3/6. Employees are happy!
"""

employee_happiness = input().split(" ")
happiness_factor = int(input())

employees = list(map(lambda x: int(x) * happiness_factor, employee_happiness)) # multipling all list of employees by the happines and turns the list into int
filtered = list(filter(lambda x: (x >= sum(employees)/len(employees)), employees)) #if current employee happines is equal or greater filter it


if len(filtered) >= len(employees)/2:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are not happy!")