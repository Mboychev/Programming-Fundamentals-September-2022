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