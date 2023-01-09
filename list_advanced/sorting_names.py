"""Write a program that reads a single string with names separated by comma and space ", ".
Sort the names by their length in descending order. If 2 or more names have the same length, sort them in ascending
order (alphabetically). Print the resulting list.
###################################EXAMPLES#######################################
Input: Ali, Marry, Kim, Teddy, Monika, John
Output: ["Monika", "Marry", "Teddy", "John", "Ali", "Kim"]

Input: Lilly, Tim, Kate, Tom, Alex
Output: ['Lilly', 'Alex', 'Kate', 'Tim', 'Tom']
"""

names = input()

sorted_nums = sorted(names.split(", "), key=lambda x: (-(len(x)), x))

print(sorted_nums)
