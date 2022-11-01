josephus_permutation_list = input().split(" ")
skipped_number = int(input())
josephus_permutation_list_in_int = []
final_result = []
index_counter = 0
current_list = []
len_counter = 0
for josephus_number in josephus_permutation_list:
    josephus_permutation_list_in_int.append(int(josephus_number))

while len(josephus_permutation_list_in_int) != 0:

    for index, current_number in enumerate(josephus_permutation_list_in_int):
            index_counter += 1
            len_counter += 1

            if index_counter % skipped_number == 0:
                final_result.append(current_number)
                josephus_permutation_list_in_int[index] = "None"


            if len_counter == len(josephus_permutation_list_in_int):
                len_counter = 0
                for word in josephus_permutation_list_in_int:
                    if word == "None":
                        josephus_permutation_list_in_int.remove(word)

print(str(final_result).replace(' ', ''))