single_string_list = input().split(", ")
int_lst = []
zero_counter = 0

for number in single_string_list:
    number = int(number)
    int_lst.append(number)

for current_number in int_lst:
    if current_number == 0:
        int_lst.remove(current_number)
        int_lst.append(0)

print(int_lst)