
def rounding(b):

    a = b.split(" ")
    b = []
    for current_number in a:
        a = float(current_number)
        b.append(round(a))
    return b

numbers = input()


print(rounding(numbers))