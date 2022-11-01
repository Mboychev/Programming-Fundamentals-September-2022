starting_deck = input().split(" ")
count_shuffles = int(input())


for shuffle in range(count_shuffles):
    final_deck = []
    middle_of_the_deck = len(starting_deck) // 2
    left_part = starting_deck[:middle_of_the_deck]
    right_part = starting_deck[middle_of_the_deck:]

    for index in range(len(left_part)):
        final_deck.append(left_part[index])
        final_deck.append(right_part[index])

    starting_deck = final_deck

print(final_deck)