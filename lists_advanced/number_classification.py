def positive_func(numbers):
    result = [str(x) for x in numbers if x >= 0]
    return result


def negative_func(numbers):
    result = [str(x) for x in numbers if x < 0]
    return result


def even_func(numbers):
    result = [str(x) for x in numbers if x % 2 == 0]
    return result


def odd_func(numbers):
    result = [str(x) for x in numbers if x % 2 != 0]
    return result


data = [int(num) for num in input().split(", ")]

print(f"Positive: {', '.join(positive_func(data))}")
print(f"Negative: {', '.join(negative_func(data))}")
print(f"Even: {', '.join(even_func(data))}")
print(f"Odd: {', '.join(odd_func(data))}")



