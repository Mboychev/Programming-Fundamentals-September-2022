"""Write a program that reads different floating-point numbers from the console. When it receives a number between
1 and 100 inclusive, the program should stop reading and should print "The number {number} is between 1 and 100".

###################################EXAMPLES#######################################
Input:
-3
0.9
44

Output: The number 44.0 is between 1 and 100

Input:
0.5
90
-4
101

Output: The number 90.0 is between 1 and 100"""

number = float(input())

while True:

    if 1 <= number <= 100:
        print(f"The number {number} is between 1 and 100")
        break
    number = float(input())