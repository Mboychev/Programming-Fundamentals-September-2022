def exchange_func(data, current_index):
    if 0 > current_index or current_index > len(data):
        print("Invalid index")
    else:
        data = data[current_index + 1:] + data[:current_index + 1]
    return data


def max_func(data, max_odd_even):

    if max_odd_even == "even":
        lst_even = list(filter(lambda x: x % 2 == 0, data))
        max_even_index = 0
        if lst_even:
            max_even = max(lst_even)
            for current_even_index in range(len(data)):
                if max_even == data[current_even_index]:
                    max_even_index = current_even_index
            print(max_even_index)
        else:
            print("No matches")

    elif max_odd_even == "odd":
        lst_odd = list(filter(lambda x: x % 2 != 0, data))
        max_odd_index = 0
        if lst_odd:
            max_odd = max(lst_odd)
            for current_odd_index in range(len(data)):
                if max_odd == data[current_odd_index]:
                    max_odd_index = current_odd_index
            print(max_odd_index)
        else:
            print("No matches")
    return data


def min_func(data, min_odd_even):
    if min_odd_even == "even":
        lst_even = list(filter(lambda x: x % 2 == 0, data))
        min_even_index = 0
        if lst_even:
            min_even = min(lst_even)
            for current_even_index in range(len(data)):
                if min_even == data[current_even_index]:
                    min_even_index = current_even_index
            print(min_even_index)
        else:
            print("No matches")

    elif min_odd_even == "odd":
        lst_odd = list(filter(lambda x: x % 2 != 0, data))
        min_odd_index = 0
        if lst_odd:
            min_odd = min(lst_odd)
            for current_odd_index in range(len(data)):
                if min_odd == data[current_odd_index]:
                    min_odd_index = current_odd_index
            print(min_odd_index)
        else:
            print("No matches")
    return data


def first_func(data, num_count, odd_even):
    odd_count = []
    even_count = []
    if odd_even == "odd":
        lst_odd = list(filter(lambda x: x % 2 != 0, data))
        if lst_odd:
            if num_count > len(data):
                print("Invalid count")
            else:
                for current_odd in range(len(lst_odd)):
                    if current_odd == num_count:
                        break
                    else:
                        odd_count.append(lst_odd[current_odd])
                print(odd_count)
        else:
            print(lst_odd)
    elif odd_even == "even":
        lst_even = list(filter(lambda x: x % 2 == 0, data))
        if lst_even:
            if num_count > len(data):
                print("Invalid count")
            else:
                for current_even in range(len(lst_even)):
                    if current_even == num_count:
                        break
                    else:
                        even_count.append(lst_even[current_even])
                print(even_count)
        else:
            print(lst_even)
    return data


def last_func(data, num_count, odd_even):
    odd_count = []
    even_count = []
    if odd_even == "odd":
        lst_odd = list(filter(lambda x: x % 2 != 0, data))
        lst_odd.reverse()
        if lst_odd:
            if num_count > len(data):
                print("Invalid count")
            else:
                for current_odd in range(len(lst_odd)):
                    if current_odd == num_count:
                        break
                    else:
                        odd_count.append(lst_odd[current_odd])
                odd_count.reverse()
                print(odd_count)
        else:
            print(lst_odd)
    elif odd_even == "even":
        lst_even = list(filter(lambda x: x % 2 == 0, data))
        lst_even.reverse()
        if lst_even:
            if num_count > len(data):
                print("Invalid count")
            else:
                for current_even in range(len(lst_even)):
                    if current_even == num_count:
                        break
                    else:
                        even_count.append(lst_even[current_even])
                even_count.reverse()
                print(even_count)
        else:
            print(lst_even)
    return data


data_list = list(map(int, input().split()))

while True:

    input_data = input().split()
    command = input_data[0]
    if command == "end":
        break

    elif command == "exchange":
        index = int(input_data[1])
        data_list = exchange_func(data_list, index)

    elif command == "max":
        even_odd = input_data[1]
        data_list = max_func(data_list, even_odd)

    elif command == "min":
        even_odd = input_data[1]
        data_list = min_func(data_list, even_odd)

    elif command == "first":
        count = int(input_data[1])
        even_odd = input_data[2]
        data_list = first_func(data_list, count, even_odd)

    elif command == "last":
        count = int(input_data[1])
        even_odd = input_data[2]
        data_list = last_func(data_list, count, even_odd)

print(data_list)