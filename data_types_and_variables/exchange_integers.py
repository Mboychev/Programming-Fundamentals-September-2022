"""Read two integer numbers and, after that, exchange their values.
Print the variable values before and after the exchange, as shown below:
###################################EXAMPLES#######################################
Input:
5
10

Output:
Before:
a = 5
b = 10
After:
a = 10
b = 5

Input:
10
20

Output:
Before:
a = 10
b = 20
After:
a = 20
b = 10

"""

a = int(input())
b = int(input())

print(f"Before:\na = {a}\nb = {b}")

temp = a
a = b
b = temp

print(f"After:\na = {a}\nb = {b}")
