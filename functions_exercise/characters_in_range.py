"""Write a function that receives two characters and returns a single string with all the characters in between them
(according to the ASCII code), separated by a single space. Print the result on the console.
###################################EXAMPLES#######################################
Input:
a
d
Output: b c

Input:
#
:
Output: $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9

Input:
#
C
Output: $ % & ' ( ) * + , - . / 0 1 2 3 4 5 6 7 8 9 : ; < = > ? @ A B
"""


def between_numbers(char1, char2):
    for i in range(ord(char1) + 1, ord(char2)):
        result = chr(i)
        print(f"{result}", end=" ")


character_one = input()
character_two = input()
between_numbers(character_one, character_two)