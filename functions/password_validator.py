def lenght_validation(password):
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
    else:
        return True


def letter_number_validation(password):
    if password.isalnum() == False:
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
password_is_valid = [lenght_validation(user_password), letter_number_validation(user_password), digit_validation(user_password)]

if all(password_is_valid):
    print("Password is valid")


