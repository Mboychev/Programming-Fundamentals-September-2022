current_string = input()
current_number = int(input())

repeating_string = lambda a, b: a * b

result = repeating_string(current_string, current_number)
print(result)