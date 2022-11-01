total_numbers = int(input())
total_sum = 0

# if 0 <= total_numbers <= 20:
for number in range(total_numbers):

    character = input()

    character_in_num = ord(character)
    total_sum += character_in_num

print(f"The sum equals: {total_sum}")
