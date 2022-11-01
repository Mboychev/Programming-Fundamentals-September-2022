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