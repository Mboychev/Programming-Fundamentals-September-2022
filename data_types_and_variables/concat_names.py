"""Write a program that reads two names and a delimiter. It should print the names joined by the delimiter.
###################################EXAMPLES#######################################
Input:
John
Smith
->
Output: John->Smith."""

first_name, second_name, delimiter = input(), input(), input()
print(f"{first_name}{delimiter}{second_name}")