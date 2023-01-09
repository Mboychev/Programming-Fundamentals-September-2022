"""Create a function that receives three parameters, calculates a result depending on the given operator, and returns
it. Print the result of the function.
The input comes as three parameters – an operator as a string and two integer numbers.
The operator can be one of the following:  "multiply", "divide", "add", "subtract".
###################################EXAMPLES#######################################
Input:
subtract
5
4
Output: 1

Input:
divide
8
4
Output: 2"""


def calculator(operator, num1, num2):
    if operator == "add":
        print(num1 + num2)

    elif operator == "subtract":
        print(num1 - num2)

    elif operator == "multiply":
        print(num1*num2)

    elif operator == "divide":
        print(int(num1 / num2))


current_operator = input()
n1 = int(input())
n2 = int(input())

calculator(current_operator, n1, n2)