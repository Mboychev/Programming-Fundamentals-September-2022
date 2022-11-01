def sum_numbers(num1, num2):
    result = num1 + num2
    return result


def subtract(n1, n2):
    result = n1 - n2
    return result


def add_and_subtract(nu1, nu2, nu3,):
    result = subtract(sum_numbers(nu1, nu2), nu3)
    return result


number_one = int(input())
number_two = int(input())
number_three = int(input())

print(add_and_subtract(number_one, number_two, number_three))