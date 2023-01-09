"""Write a program that counts all characters in a string except for space (" ").
Print all the occurrences in the following format:
"{char} -> {occurrences}"
###################################EXAMPLES#######################################
Input: text
Output:
t -> 2
e -> 1
x -> 1

Input: text text text
Output:
t -> 6
e -> 3
x -> 3
"""


data = input().split()
joined_data = ''.join(data)
dict = {}
occurrences = 0

for letter in joined_data:
    if letter not in dict.keys():
        dict[letter] = 0
    dict[letter] += 1

for index, value in dict.items():
    print(f"{index} -> {value}")

