"""You are a mad scientist, and you have decided to play with electron distribution among atom shells.
The basic idea of electron distribution is that electrons should fill a shell until it holds the maximum number of
electrons.
You will receive a single integer - the number of electrons. Your task is to fill shells until there are no more
electrons left. The rules for electron distribution are as follows:
•	The maximum number of electrons in a shell can be 2n2, where n is the position of a shell (starting from 1).
For example, the maximum number of electrons in the 3rd shield can be 2*32 = 18.
•	You should start filling the shells from the first one at the first position.
•	If the electrons are enough to fill the first shell, the left unoccupied electrons should fill the following
shell and so on.
In the end, print a list with the filled shells.
###################################EXAMPLES#######################################
Input: 10
Output: [2, 8]

Input: 44
Output: [2, 8, 18, 16]
"""


number_of_electrons = int(input())

shells = number_of_electrons * [0]
index = 0

total_electrons = number_of_electrons

for current_index in range(1, len(shells)):
    if total_electrons <= 0:
        break

    current_calc = 2 * (current_index ** 2)

    if total_electrons >= current_calc:
        shells[current_index] = current_calc
    else:
        shells[current_index] = abs(total_electrons)
    total_electrons -= current_calc
for number in range(len(shells)):
    if 0 in shells:
        shells.remove(0)

print(shells)

