"""Write a function that calculates the total price of an order and returns it. The function should receive one of the following products: "coffee", "coke", "water", or "snacks", and a quantity of the product. The prices for a single piece of each product are:
•	coffee - 1.50
•	water - 1.00
•	coke - 1.40
•	snacks - 2.00

Print the result formatted to the second decimal place.
###################################EXAMPLES#######################################
Input:
water
5
Output: 5.00

Input:
coffee
2
Output: 3.00
"""


def vending_machine(product, quantity):

    if product == "coffee":
        return 1.5 * quantity

    elif product == "water":
        return 1.00 * quantity

    elif product == "coke":
        return 1.4 * quantity

    elif product == "snacks":
        return 2.00 * quantity


current_product = input()
current_quantity = int(input())

print(f"{vending_machine(current_product, current_quantity):.2f}")