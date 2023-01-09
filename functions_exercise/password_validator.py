"""Write a function that checks if a given password is valid. Password validations are:
•	It should be 6 - 10 (inclusive) characters long
•	It should consist only of letters and digits
•	It should have at least 2 digits
If a password is valid, print "Password is valid".
Otherwise, for every unfulfilled rule, print a message:
•	"Password must be between 6 and 10 characters"
•	"Password must consist only of letters and digits"
•	"Password must have at least 2 digits"
###################################EXAMPLES#######################################
Input: logIn
Output:
Password must be between 6 and 10 characters
Password must have at least 2 digits

Input: MyPass123
Output: Password is valid

Input: Pa$s$s
Output:
Password must consist only of letters and digits
Password must have at least 2 digits
"""


def length_validation(password):
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
    else:
        return True


def letter_number_validation(password):
    if not password.isalnum():
        print("Password must consist only of letters and digits")
    else:
        return True


def digit_validation(password):
    number_counter = 0
    for current_char in password:
        if str.isdigit(current_char):
            number_counter += 1

    if number_counter < 2:
        print("Password must have at least 2 digits")
        return False
    return True


user_password = input()
password_is_valid = [length_validation(user_password), letter_number_validation(user_password), digit_validation(user_password)]

if all(password_is_valid):
    print("Password is valid")


