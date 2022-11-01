# def smallest_integer(num1, num2, num3):
#     a = min(first_number, second_number, third_number)
#     return a
#
# first_number = int(input())
# second_number = int(input())
# third_number = int(input())
#
# print(smallest_integer(first_number, second_number, third_number))

first_number = int(input())
second_number = int(input())
third_number = int(input())

result = lambda a, b, c: min(a, b, c)
print(result(first_number, second_number, third_number))