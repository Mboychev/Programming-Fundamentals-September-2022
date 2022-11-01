first_line = int(input())

for _ in range(first_line):

    number = int(input())

    if not number % 2 == 0:
        print(f"{number} is odd!")
        break

else:
    print("All numbers are even.")