"""This problem takes its name from arguably the most important event in the life of the ancient historian Josephus.
According to his tale, he and his 40 soldiers were trapped in a cave by the Romans during a siege. Refusing to surrender
to the enemy, they instead opted for mass suicide, with a twist: they formed a circle and proceeded to kill one man of
every three until one last man was left (and that it was supposed to kill himself to end the act). Well, Josephus and
another man were the last, and, as we now know every detail of the story, you may have correctly guessed that they did
not precisely follow through with the original idea.
You are now to create a program that prints a Josephus permutation, receiving two lines of code:
•	the list itself - numbers separated by a single space representing the people in the circle
•	a number k
People are standing in a circle waiting to be executed. Counting begins from the first one in the circle and proceeds
from left to right. After a specified number of people are skipped, the k person is executed. The procedure is repeated
with the remaining people, starting with the next person, going in the same direction, and skipping the same number of
people until no one remains.
Print the people by order of executions in the format: "[{executed1},{executed2}, … {executedN}]"
###################################EXAMPLES#######################################
Input:
1 2 3 4 5 6 7
3
Output: [3,6,2,7,5,1,4]

Input:
10 5 65 104 1 0 2
8
Output: [10,65,0,1,5,2,104]"""

josephus_permutation_list = input().split(" ")
skipped_number = int(input())
josephus_permutation_list_in_int = []
final_result = []
index_counter = 0
current_list = []
len_counter = 0
for josephus_number in josephus_permutation_list:
    josephus_permutation_list_in_int.append(int(josephus_number))

while len(josephus_permutation_list_in_int) != 0:

    for index, current_number in enumerate(josephus_permutation_list_in_int):
        index_counter += 1
        len_counter += 1

        if index_counter % skipped_number == 0:
            final_result.append(current_number)
            josephus_permutation_list_in_int[index] = "None"

        if len_counter == len(josephus_permutation_list_in_int):
            len_counter = 0
            for word in josephus_permutation_list_in_int:
                if word == "None":
                    josephus_permutation_list_in_int.remove(word)

print(str(final_result).replace(' ', ''))