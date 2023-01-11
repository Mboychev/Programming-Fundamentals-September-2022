"""Write a program that reads a string from the console and replaces any sequence of the same letters with
a single corresponding letter.
###################################EXAMPLES#######################################
Input: aaaaabbbbbcdddeeeedssaa
Output: abcdedsa

Input: qqqwerqwecccwd
Output: qwerqwecwd
"""

text = input()
replaced_text = text[0]

for index in range(len(text)):
    if index + 1 < len(text):
        if text[index] != text[index + 1]:
            replaced_text += text[index + 1]

print(replaced_text)