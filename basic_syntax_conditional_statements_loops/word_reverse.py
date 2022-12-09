""""Write a program that receives a single word, reverses it, and prints it.

###################################EXAMPLES#######################################
Input: Python
Output: nohtyP

Input: banana
Output: ananab"""

word = input()
reversed_word = ""

for i in range(len(word) -1, -1, -1):
    reversed_word += word[i]

print(reversed_word)

# word = input()
#
# print(word[:: -1])