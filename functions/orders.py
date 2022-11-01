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