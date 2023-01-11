""""Write a program that calculates the total cost of bought furniture. You will be given information about each
purchase on separate lines until you receive the command "Purchase". Valid information should be in the format:
 ">>{furniture_name}<<{price}!{quantity}". The price could be a floating-point or integer number. You should store
the names of the furniture and the total price.
In the end, print the name of each bought furniture and the total cost, formatted to the second decimal point:
"Bought furniture:
{1st name}
{2nd name}
…
{N name}
Total money spend: {total_cost}"
###################################EXAMPLES#######################################
Input:
>>Sofa<<312.23!3
>>TV<<300!5
>Invalid<<!5
Purchase
Output:
Bought furniture:
Sofa
TV
Total money spend: 2436.69
"""

import re

pattern = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
furniture_list = []
total_price = 0
while True:

    purchase = input()

    if purchase == "Purchase":
        break

    match = re.search(pattern, purchase)
    if match:
        furniture, price, quantity = match.groups()
        total_price += float(price) * int(quantity)
        furniture_list.append(furniture)
print("Bought furniture:")

for current_print in furniture_list:
    print(current_print)
print(f"Total money spend: {total_price:.2f}")