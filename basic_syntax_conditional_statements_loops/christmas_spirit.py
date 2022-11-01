# quantity_of_decoration = int(input())
# days_until_christmass = int(input())
#
# ornament_set_price = 2
# tree_skirt_price = 5
# tree_garland_price = 3
# tree_lights_price = 15
#
# ornament_set_total = 0
# tree_skirt_total = 0
# tree_garland_total = 0
# tree_lights_total = 0
#
# total_spirit = 0
# total_cost = 0
# skirts_garlands = False
# current_day = 0
#
# for day in range(days_until_christmass):
#
#     current_day += 1
#
#     if current_day % 11 == 0:
#         quantity_of_decoration += 2
#
#     if current_day % 2 == 0:
#         ornament_set_total = ornament_set_price * quantity_of_decoration
#         total_cost += ornament_set_total
#         total_spirit += 5
#
#     if current_day % 3 == 0:
#         tree_skirt_total = tree_skirt_price * quantity_of_decoration + tree_garland_price * quantity_of_decoration
#         total_spirit += 13
#         total_cost = total_cost + tree_garland_total + tree_skirt_total
#
#     if current_day % 5 == 0:
#         tree_lights_total = tree_lights_price * quantity_of_decoration
#         total_spirit += 17
#         total_cost += tree_lights_total
#
#         if skirts_garlands == True:
#             total_spirit += 30
#
#     if current_day % 10 == 0:
#         total_spirit -= 20
#         total_cost = total_cost + tree_skirt_price + tree_garland_price + tree_lights_price
#
#     if days_until_christmass == 10 and days_until_christmass < 10:
#         total_spirit -= 30
#
#
# print(f"Total cost: {total_cost}")
# print(f"Total spirit: {total_spirit}")
python
