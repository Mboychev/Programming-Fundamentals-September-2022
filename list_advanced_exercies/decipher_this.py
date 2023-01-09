"""You are given a secret message you should decipher. To do that, you need to know that in each word:
•	the second and the last letter are switched (e.g., Holle means Hello)
•	the first letter is replaced by its character code (e.g., 72 means H)
###################################EXAMPLES#######################################
Input: 72olle 103doo 100ya
Output: Hello good day

Input: 82yade 115te 103o
Output: Ready set go
"""
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
