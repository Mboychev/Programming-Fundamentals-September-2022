"""On the first line, you will receive a sequence of numbers separated by a single space. On the second line,
you will receive a string. Your task is to write a program that sends a message only using chars from the given
string. Each char the program adds to the message should be found by its index. The index you are looking for
is the sum of a number's digits from the first sequence. If the index is greater than the length of the text,
continue counting from the beginning (so that you always have a valid index). When you find a char,
you should add it to the message and remove it from the string. It means that for the following index,
the text will contain one character less.
Print the final message.

###################################EXAMPLES#######################################
Input:
9992 562 8933
This is some message for you
Output: hey

Input:
2 122 1123 1321 9 17211
87j973u59dg37e725!

Output: judge!"""

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