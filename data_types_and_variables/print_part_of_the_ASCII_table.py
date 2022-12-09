"""Write a program that prints part of the ASCII table characters on the console, separated by a single space.
On the first line of input, you will receive the char index you should start with. On the second line - the index of
the last character you should print.
Input:
60
65

Output: < = > ? @ A

Input:
69
79

Output: E F G H I J K L M N O

Input:
97
104

Output: a b c d e f g h

Input:
40
55

Output: ( ) * + , - . / 0 1 2 3 4 5 6 7
"""

start_character = int(input())
last_character = int(input())

for number in range(start_character, last_character + 1):
    d = chr(number)
    print(d, end=" ")