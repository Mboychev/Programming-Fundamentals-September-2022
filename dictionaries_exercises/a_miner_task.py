"""You will be given a sequence of strings, each on a new line until you receive the "stop" command.
Every odd line on the console represents a resource (e.g., Gold, Silver, Copper, and so on) and
every even - quantity. Your task is to collect the resources and print them each on a new line.
Print the resources and their quantities in the following format:
"{resource} -> {quantity}"
The quantities will be in the range [1 … 2 000 000 000].
###################################EXAMPLES#######################################
Input:
Gold
155
Silver
10
Copper
17
stop

Output:
Gold -> 155
Silver -> 10
Copper -> 17

Input:
gold
155
silver
10
copper
17
gold
15
stop
Output:
gold -> 170
silver -> 10
copper -> 17
"""


total_resources = {}

while True:

    current_resources = input()

    if current_resources == "stop":
        break

    current_quantity = int(input())

    if current_resources not in total_resources.keys():

        total_resources[current_resources] = 0
    total_resources[current_resources] += current_quantity

for resources, quantity in total_resources.items():
    print(f"{resources} -> {quantity}")