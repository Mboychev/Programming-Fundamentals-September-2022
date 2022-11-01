line_number = int(input())

for i in range(line_number):

    number = int(input())

    if number == 88:
        print("Hello")

    elif number == 86:
        print("How are you?")

    elif number <= 88:
        if number != 86 or number !=88:
            print("GREAT!")

    else:
        print("Bye.")
