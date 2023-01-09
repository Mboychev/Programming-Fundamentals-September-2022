"""After you have completed your first task, your boss decides to give you another one right away.
Now not only you have to keep track of the stock, but also you should answer customers if
you have some products in stock or not.
You will be given key-value pairs of products and quantities (on a single line separated by space).
On the following line, you will be given products to search for. Check for each product. You have 2 possibilities:
•	If you have the product, print "We have {quantity} of {product} left".
•	Otherwise, print "Sorry, we don't have {product}".

###################################EXAMPLES#######################################
Input:
cheese 10 bread 5 ham 10 chocolate 3
jam cheese ham tomatoes

Output:
Sorry, we don't have jam
We have 10 of cheese left
We have 10 of ham left
Sorry, we don't have tomatoes

Input:
eggs 5 bread 10
bread eggs
Output:
We have 10 of bread left
We have 5 of eggs left
"""


data = input().split()
searched_data = input().split()
bakery = {}

for index in range(0, len(data), 2):

    key = data[index]
    value = data[index + 1]
    bakery[key] = int(value)

for product in searched_data:
    if product in bakery:
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")