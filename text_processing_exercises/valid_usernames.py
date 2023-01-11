"""Write a program that reads usernames on a single line (separated by ", ")
and prints all valid usernames on separate lines.
A valid username:
•	has length between 3 and 16 characters inclusive
•	can contain only letters, numbers, hyphens, and underscores
•	has no redundant symbols before, after, or in between
###################################EXAMPLES#######################################
Input: sh, too_long_username, !lleg@l ch@rs, jeffbutt
Output: jeffbutt

Input: Jeff, john45, ab, cd, peter-ivanov, @smith
Output:
Jeff
John45
peter-ivanov
"""


def len_validation(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def chars_are_valid(name):
    for letter in name:
        if not (letter.isalnum() or letter == "-" or letter == "_"):
            return False
    return True


def no_redundant(name):
    if " " in name:
        return False
    return True


def username_validation(name):
    if len_validation(name) and chars_are_valid(name) and no_redundant(name):
        return True
    return False


usernames = input().split(", ")

for user in usernames:
    if username_validation(user):
        print(user)



