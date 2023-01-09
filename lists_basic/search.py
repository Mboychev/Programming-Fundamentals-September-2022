"""On the first line, you will receive a number n. On the second line, you will receive a word.
On the following n lines, you will be given some strings. You should add them to a list and print them.
After that, you should filter out only the strings that include the given word and print that list too.
###################################EXAMPLES#######################################
Input:
3
SoftUni
I study at SoftUni
I walk to work
I learn Python at SoftUni

Output:
["I study at SoftUni", "I walk to work", "I learn Python at SoftUni"]
["I study at SoftUni", "I learn Python at SoftUni"]


Input:
4
tomatoes
I love tomatoes
I can eat tomatoes forever
I don't like apples
Yesterday I ate two tomatoes

Output:
["I love tomatoes", "I can eat tomatoes forever", "I don't like apples", "Yesterday I ate two tomatoes"]
["I love tomatoes", "I can eat tomatoes forever", "Yesterday I ate two tomatoes"]
"""

number_of_lines = int(input())
word = input()
lst_words = []
filtered_words = []

for _ in range(number_of_lines):

    current_string = input()
    lst_words.append(current_string)

    if word in current_string:
        filtered_words.append(current_string)


print(lst_words)
print(filtered_words)