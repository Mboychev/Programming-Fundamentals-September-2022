"""Write a program that returns an encrypted version of the same text.
Encrypt the text by replacing each character with the corresponding character three positions forward
in the ASCII table. For example, A would be replaced with D, B would become E, and so on. Print the encrypted text.
###################################EXAMPLES#######################################
Input: Programming is cool!
Output: Surjudpplqj#lv#frro$

Input: One year has 365 days.
Output: Rqh#|hdu#kdv#698#gd|v1
"""

text = input()
encrypted_text = ""

for current_letter in text:
    encrypted_text = chr(ord(current_letter) + 3)
    print(encrypted_text, end="")
