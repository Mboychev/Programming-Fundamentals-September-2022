from math import ceil
capacity_of_elevator = int(input())
number_of_people = int(input())

courses = capacity_of_elevator / number_of_people

print(ceil(courses))





