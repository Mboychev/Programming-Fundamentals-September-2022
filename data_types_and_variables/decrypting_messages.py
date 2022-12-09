"""On the first line, you will receive a key (integer). On the second line, you will receive n – the number of lines,
which will follow. On the next n lines – you will receive a lower and an uppercase letter per line.
You should add the key to each of the characters and append them to a message. In the end, print the decrypted message.
###################################EXAMPLES#######################################
Input:
3
7
P
l
c
q
R
k
f

Output: SoftUni

Input:
1
7
C
d
b
q
x
o
s

Output: Decrypt
"""

key = int(input())
number_of_lines = int(input())

for letter in range(number_of_lines):

    input_letter = input()
    letter_ascii = ord(input_letter)
    new_letter = letter_ascii + key
    decrypted = chr(new_letter)
    print(f"{decrypted}", end="")
