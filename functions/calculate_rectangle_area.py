"""Create a function that calculates and returns the area of a rectangle by given width and height.
Print the result on the console.
###################################EXAMPLES#######################################
Input:
3
4
Output: 12

Input:
6
2
Output: 12"""

width = int(input())
height = int(input())

result = lambda a, b: a * b

print(result(width, height))