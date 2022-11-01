key = int(input())
number_of_lines = int(input())

for letter in range(number_of_lines):

    input_letter = input()
    letter_ascii = ord(input_letter)
    new_letter = letter_ascii + key
    decripted = chr(new_letter)
    print(f"{decripted}", end="")
