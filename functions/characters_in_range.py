def between_numbers(char1, char2):
    for i in range(ord(char1) + 1, ord(char2)):
        result = chr(i)
        print(f"{result}", end=" ")


character_one = input()
character_two = input()
between_numbers(character_one, character_two)