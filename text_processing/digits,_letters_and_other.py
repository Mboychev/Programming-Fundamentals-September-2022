"""Write a program that receives a single string.
On the first line, print all the digits found in the string, on the second – all the letters, and
on the third – all the other characters. There will always be at least one digit, one letter, and one other character
###################################EXAMPLES#######################################
Input: Agd#53Dfg^&4F53
Output:
53453
AgdDfgF
#^&
"""

single_string = input()
digits, letters, others = [], [], []

for current_symbol in single_string:

    if current_symbol.isdigit():
        digits.append(current_symbol)

    elif current_symbol.isalpha():
        letters.append(current_symbol)

    else:
        others.append(current_symbol)

print(f"{''.join(digits)}\n{''.join(letters)}\n{''.join(others)}\n")
