"""Write a program that converts British pounds (integer) to US dollars formatted to the 3rd decimal point.
1 British Pound = 1.31 Dollars.
###################################EXAMPLES#######################################
Input: 80
Output: 104.800

Input: 39
Output: 51.090
"""

pounds = int(input())

dollars = pounds * 1.31
print(f"{dollars:.3f}")


# from forex_python.converter import CurrencyRates
#
# c = CurrencyRates()
#
# amount = int(input())
#
# current_rate = c.get_rate('GBP', 'USD')
#
# output = current_rate * amount
#
# print(f"{output:.3f}")
