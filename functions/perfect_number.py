def perfect_number(number):
    total_sum = 0
    for current_number in range(1, number + 1):
        if number % current_number == 0:
            total_sum += current_number
    if total_sum / 2 == number:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

user_number = int(input())

perfect_number(user_number)