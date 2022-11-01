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