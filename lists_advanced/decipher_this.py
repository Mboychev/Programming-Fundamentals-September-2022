message = input().split()

for word in message:

    numbers = []
    current_letters = []
    for letter in word:
        if letter.isdigit():
            numbers.append(letter)
        else:
            current_letters.append(letter)

    current_letters[0], current_letters[-1] = current_letters[-1],  current_letters[0]
    current_number, current_letters = "".join(numbers), "".join(current_letters)
    num_in_letter = chr(int(current_number))
    print(num_in_letter + current_letters, end=" ")











    # numbers = [letter.isdigit() for letter in word]
