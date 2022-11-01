def palindrome_check(number):

    for current_number in number:
        turned_number = current_number[::-1]
        if turned_number == current_number:
            print(True)
        else:
            print(False)


list_of_numbers = input().split(", ")
palindrome_check(list_of_numbers)