numbers = input().split(" ")
chars = input()
final_lst = []
digit_counter = 0
new_lst = []

for current_number in (numbers):
   number_sum = 0
   for digits in range(len(current_number)):
        number_sum += int(current_number[digits])

   new_lst.append(number_sum)

for index, current_numbers_sum in enumerate(new_lst):

    if len(chars) > current_numbers_sum:

        index_for_termination = current_numbers_sum
    else:
        index_for_termination = current_numbers_sum - len(chars)

    final_lst.append(chars[index_for_termination + digit_counter])
    digit_counter += 1

for i in final_lst:
    print(i, end="")