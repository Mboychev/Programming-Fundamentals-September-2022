"""Write a program to read an integer N and print all triples of the first N small Latin letters,
ordered alphabetically:
###################################EXAMPLES#######################################
Input: 3
Output:
aaa
aab
aac
aba
abb
abc
aca
acb
acc
baa
bab
bac
bba
bbb
bbc
bca
bcb
bcc
caa
cab
cac
cba
cbb
cbc
cca
ccb
ccc

Input: 2
Output:
aaa
aab
aba
abb
baa
bab
bba
bbb
"""
number = int(input())

for i in range(number):
    for j in range(number):
        for k in range(number):
            print(f"{chr(97+i)}{chr(97+j)}{chr(97+k)}")
