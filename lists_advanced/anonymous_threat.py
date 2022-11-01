def merge_func(start_index, end_index, text):

    conc = ''
    if end_index > len(text):
        end_index = len(text) - 1
    if start_index <= len(text):
        for index in range(start_index, end_index + 1):
            conc += text[index]
        text[start_index] = conc
        for index in range(end_index, start_index, -1):
            text.pop(index)

    return text


def divide_func(index, partitions, text):

    for current_word in range(len(text)):
        if current_word == index:

            a = text[current_word]
            b = int(len(a)//partitions)
            parts = [a[i:i + b] for i in range(0, len(a), b)]
            text.pop(index)
            text[index:index] = parts
    return text


array_of_data = input().split(" ")

while True:

    data = input()

    if data == "3:1":
        break

    command, first_num, second_num = data.split(" ")

    if command == "merge":
        result = merge_func(int(first_num), int(second_num), array_of_data)

    elif command == "divide":
        result = divide_func(int(first_num), int(second_num), array_of_data)



print(" ".join(result))

