"""A perfect number is a positive integer that is equal to the sum of its proper positive divisors. That is the sum of its positive divisors, excluding the number itself (also known as its aliquot sum).
Write a function that receives an integer number and returns one of the following messages:
•	"We have a perfect number!" - if the number is perfect.
•	"It's not so perfect." - if the number is NOT perfect.
Print the result on the console.
###################################EXAMPLES#######################################
Input: 6
Output: We have a perfect number!

Input: 28
Output: We have a perfect number!

Input: 1236498
Output: It's not so perfect."""


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