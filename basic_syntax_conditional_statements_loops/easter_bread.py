budget = float(input())
flour_price_per_kg = float(input())

egg_pack_price = flour_price_per_kg * 0.75
milk_per_liter = flour_price_per_kg * 1.25
current_bread_count = 0
color_eggs_count = 0

if 0 <= budget < 100000 and 0 <= flour_price_per_kg < 100000:

    while True:

        if budget > 0:
            plus_color_eggs_count = 0
            price_per_loaf_of_bread = egg_pack_price + flour_price_per_kg + (milk_per_liter/4)
            if budget < price_per_loaf_of_bread:
                break
            color_eggs_count += 3
            budget -= price_per_loaf_of_bread
            current_bread_count += 1



            if current_bread_count % 3 == 0 and current_bread_count != 0:

                plus_color_eggs_count = current_bread_count - 2
                color_eggs_count -= plus_color_eggs_count


        else:
            break


print(f"You made {current_bread_count} loaves of Easter bread! Now you have {color_eggs_count} eggs and {budget:.2f}BGN left.")

