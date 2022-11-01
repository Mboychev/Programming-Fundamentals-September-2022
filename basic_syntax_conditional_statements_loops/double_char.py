while True:

    string = input()

    if string == "End":
        break
    if string == "SoftUni":
        continue

    for i in(string):

        i *= 2
        print(i, end= "")
    print(i)