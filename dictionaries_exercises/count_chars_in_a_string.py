# Write a program that counts all characters in a string except for space (" ").
# Print all the occurrences in the following format:
# "{char} -> {occurrences}"


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

