"""Write a program that finds all variable names in each string. A variable name starts with an underscore ("_")
and contains only capital and non-capital letters and digits. Extract only their names without the underscore.
Try to do this only with regular expressions.
The output consists of all variable names extracted and printed on a single line, separated by a comma.
###################################EXAMPLES#######################################
Input: The _id and _age variables are both integers.
Output: id,age

Input: alculate the _area of the _perfectRectangle object.
Output: area,perfectRectangle

Input: __invalidVariable _evenMoreInvalidVariable_ _validVariable
Output: validVariable
"""

import re

data = input()

pattern = r'\b_([A-Za-z0-9]+)\b'

match = re.findall(pattern, data)

print(','.join(match))