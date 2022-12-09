"""Write a program that reads an integer number representing a budget. On the following lines, it reads integer numbers
representing the prices of each product you should buy until it receives the command "End".
During the iterations, if there is not enough budget left to buy the next product, it prints "You went in overdraft!"
and end the program.
Otherwise, if you accomplished to buy all products before receiving "End", it prints "You bought everything needed."

###################################EXAMPLES#######################################
Input:
100
5
End

Output: You bought everything needed.

Input:
50
25
20
10

Output: You went in overdraft!"""

budget = int(input())
total = budget

while True:

    price_per_product = input()
    if price_per_product == "End":
        print("You bought everything needed.")
        break

    price_per_product = int(price_per_product)
    total -= price_per_product

    if total < 0:
        print("You went in overdraft!")
        break