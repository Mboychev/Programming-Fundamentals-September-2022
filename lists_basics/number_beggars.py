string_of_integers = input().split(", ")
count_beggars = int(input())

lst_of_sums = []
int_of_integers = []
index_counter = 0
starting_index = 0

for digits in string_of_integers:
    int_of_integers.append(int(digits))

while starting_index < count_beggars:

    current_beggar_sum = 0

    for current_index in range(starting_index, len(int_of_integers), count_beggars):

        current_beggar_sum += int_of_integers[current_index]
    lst_of_sums.append(current_beggar_sum)
    starting_index += 1

print(lst_of_sums)