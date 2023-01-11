"""Find all emoticons in the text. An emoticon always starts with ":" and is followed by a symbol.
The input will be provided as a single string.
###################################EXAMPLES#######################################
Input:There are so many emoticons nowadays :P. I have many ideas :O what input to place here :)
Output:
:P
:O
:)
"""

text = input()

for position, letter in enumerate(text):
    if letter == ":":
        if position + 1 < len(text):
            print(f"{letter}{text[position + 1]}")


