orders_number = int(input())
total = 0

for i in range(orders_number):


    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_per_day <= 2000:
        price = capsules_per_day * days * price_per_capsule
        total += price
        print(f"The price for the coffee is: ${price:.2f}")

print(f"Total: ${total:.2f}")