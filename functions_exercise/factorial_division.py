def factorial(number):
    result = 1
    for current_number in range(1, number + 1):
        result *= current_number
    return result


def division(num_one, num_two):
    result = int(num_one / num_two)
    print(f"{result:.2f}")


number_one = int(input())
number_two = int(input())

division(factorial(number_one), factorial(number_two))