"""You will be given two sequences of strings, separated by ", ". Print a new list containing only the strings from the
first input line, which are substrings of any string in the second input line.
###################################EXAMPLES#######################################
Input:
arp, live, strong
lively, alive, harp, sharp, armstrong
Output: ['arp', 'live', 'strong']

Input:
tarp, mice, bull
lively, alive, harp, sharp, armstrong
Output: []
"""

sequence_one = input().split(", ")
sequence_two = input().split(", ")

substrings = [first for first in sequence_one if any(first in second for second in sequence_two)]


# for current_word in sequence_one:
#     for current_word_a in sequence_two:
#         if current_word in current_word_a:
#             substrings.append(current_word)
#             break

print(substrings)