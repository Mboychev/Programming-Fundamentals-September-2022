# Write a program that receives a list of characters separated by ", ".
# It should create a dictionary with each character as a key and its ASCII value as a value.
# Try solving that problem using comprehension

list_of_chars = {key:ord(key) for key in input().split(", ")}
print(list_of_chars)