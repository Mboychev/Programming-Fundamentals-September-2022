"""You will be given the coordinates of two points on a Cartesian coordinate system - X1, Y1, X2, and Y2 on separate
lines. Write a function that prints the point which is closest to the center of the coordinate system (0, 0) in the
format: "({X}, {Y})"
If the points are at the same distance from the center, print only the first one. The resulting coordinates must be
formatted to the lower integer.
###################################EXAMPLES#######################################
Input:
2
4
-1
2
Output: (-1, 2)

Input:
10
14.5
-17.2
16
Output: (10, 14)
"""
from math import floor


def closest_point(x1, y1, x2, y2):

    xx1 = abs(x1)
    yy1 = abs(y1)
    xx2 = abs(x2)
    yy2 = abs(y2)
    if xx1 == xx2:
        if yy1 == yy2:
            return x1, y1
        elif yy1 > yy2:
            return x2, y2
        else:
            return x1, y1
    elif yy1 > yy2:
        return x2, y2
    else:
        return x1, y1


x_first_point = float(input())
y_first_point = float(input())
x_second_point = float(input())
y_second_point = float(input())

print(closest_point(floor(x_first_point), floor(y_first_point), floor(x_second_point), floor(y_second_point)))