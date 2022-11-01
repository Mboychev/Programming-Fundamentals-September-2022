sequence_one = input().split(", ")
sequence_two = input().split(", ")


substrings = [first for first in sequence_one if any(first in second for second in sequence_two)]




# for current_word in sequence_one:
#     for current_word_a in sequence_two:
#         if current_word in current_word_a:
#             substrings.append(current_word)
#             break

print(substrings)