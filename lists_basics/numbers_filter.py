number_of_lines = int(input())
COMMAND_EVEN = "even"
COMMAND_ODD = "odd"
COMMAND_NEGATIVE = "negative"
COMMAND_POSITIVE = "positive"

numbers = []

for i in range(number_of_lines):

    current_number = int(input())
    numbers.append(current_number)

command = input()
filtered_numbers = []
filtered_passes = []

for i in numbers:

    filtered_passes = (
        (command == COMMAND_EVEN and i % 2 == 0) \
            or (command == COMMAND_ODD and i % 2 != 0) \
            or (command == COMMAND_POSITIVE and i >= 0) \
            or (command == COMMAND_NEGATIVE and i < 0))

    if filtered_passes == True:

        filtered_numbers.append(i)

print(filtered_numbers)



