from math import floor


def longest_line(num1, num2):
    result = sum(num1) + sum(num2)
    return result


def closest_point(x1, y1, x2, y2):

    x1 = abs(x1)
    y1 = abs(y1)
    x2 = abs(x2)
    y2 = abs(y2)
    if x1 == x2:
        if y1 == y2:
            return x1, y1
        elif y1 > y2:
            return x2, y2
        else:
            return x1, y1
    elif y1 > y2:
        return x2, y2
    else:
        return x1, y1


x_first_point_line_one = float(input())
y_first_point_line_one = float(input())
x_second_point_line_one = float(input())
y_second_point_line_one = float(input())

x_first_point_line_two = float(input())
y_first_point_line_two = float(input())
x_second_point_line_two = float(input())
y_second_point_line_two = float(input())


print(closest_point(x_first_point_line_one, y_first_point_line_one, x_first_point_line_two, y_first_point_line_two))
print(closest_point(x_second_point_line_one, y_second_point_line_one, x_second_point_line_two, y_second_point_line_two))

print(longest_line(closest_point(x_first_point_line_one, y_first_point_line_one,\
                                 x_first_point_line_two, y_first_point_line_two),\
                   closest_point(x_second_point_line_one, y_second_point_line_one, x_second_point_line_two, y_second_point_line_two)))