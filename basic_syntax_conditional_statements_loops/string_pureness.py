count_strings = int(input())
pure_string = True

for i in range(count_strings):

    string = input()

    for j in (string):

        if j == "," or j == "." or j == "_":
            pure_string = False
            break
    else:
        pure_string = True

    if pure_string == False:
         print(f"{string} is not pure!")

    else:
        print(f"{string} is pure.")



