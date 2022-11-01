start_character = int(input())
last_character = int(input())

for number in range(start_character, last_character + 1):
    d = chr(number)
    print(d, end=" ")