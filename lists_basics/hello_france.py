from decimal import Decimal
items_with_prices = input().split("|")
budget = float(input())
CLOTHES_MAX_PRICE = 50.00
SHOES_MAX_PRICE = 35.00
ACCESSORIES_MAX_PRICE = 20.50
ITEM_CLOTHES = "Clothes"
ITEM_SHOES = "Shoes"
ITEM_ACCESSORIES = "Accessories"
total_sum = 0
old_sum = 0
profit = 0

for item in items_with_prices:
    splitted = item.split("->")
    price_in_float = float(splitted[-1])
    item = splitted[0]


    if budget >= price_in_float:
        if CLOTHES_MAX_PRICE >= price_in_float and ITEM_CLOTHES == item\
            or SHOES_MAX_PRICE >= price_in_float and ITEM_SHOES == item\
            or ACCESSORIES_MAX_PRICE >= price_in_float and ITEM_ACCESSORIES == item:
                old_sum += price_in_float
                budget -= price_in_float
                new_price = price_in_float * 1.4
                total_sum += new_price
                print(f"{new_price:.2f}", end=" ")

        total = total_sum + budget
        profit = total - old_sum - budget
print()
print(f"Profit: {profit:.2f}")

if total >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")