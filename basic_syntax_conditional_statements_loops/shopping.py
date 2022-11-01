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