"""Write a program that receives a number n on the first line. On the following n lines,
 it receives different integer numbers. If the program receives an odd number, print "{num} is odd!"
 and end the program. Otherwise, if all numbers given are even, print "All numbers are even.".

###################################EXAMPLES#######################################
Input:
2
12
286

Output: All numbers are even.

Input:
5
2
9

Output: 9 is odd!"""


first_line = int(input())

for _ in range(first_line):

    number = int(input())

    if not number % 2 == 0:
        print(f"{number} is odd!")
        break

else:
    print("All numbers are even.")