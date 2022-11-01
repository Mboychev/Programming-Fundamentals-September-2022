def min_max_sum(numbers):

    result = list(map(lambda x: int(x), numbers.split(" ")))
    min_number = min(result)
    max_number = max(result)
    total_number_sum = sum(result)

    return min_number, max_number, total_number_sum

sequence_of_numbers = input()
minimal, maximal, the_sum = min_max_sum(sequence_of_numbers)
print(f"The minimum number is {minimal}")
print(f"The maximum number is {maximal}")
print(f"The sum number is: {the_sum}")
