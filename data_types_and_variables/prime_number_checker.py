num = int(input())

counter = 0


for numbers in range(num, 0, -1):
    for digits in range(num, 0, -1):
        result = int(digits * numbers)
        if result == num and result % num == 0:
            counter += 1


if counter == 2:
    print("True")
else:
    print("False")
