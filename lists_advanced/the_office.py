employee_happiness = input().split(" ")
happiness_factor = int(input())

employees = list(map(lambda x: int(x) * happiness_factor, employee_happiness)) # multipling all list of employees by the happines and turns the list into int
filtered = list(filter(lambda x: (x >= sum(employees)/len(employees)), employees)) #if current employee happines is equal or greater filter it


if len(filtered) >= len(employees)/2:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(employees)}. Employees are not happy!")