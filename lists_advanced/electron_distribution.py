number_of_electrons = int(input())

shells = number_of_electrons * [0]
index = 0

total_electrons = number_of_electrons

for current_index in range(1, len(shells)):
    if total_electrons <= 0:
        break

    current_calc = 2 * ((current_index) ** 2)

    if total_electrons >= current_calc:
        shells[current_index] = current_calc
    else:
        shells[current_index] = abs(total_electrons)
    total_electrons -= current_calc
for number in range(len(shells)):
    if 0 in shells:
        shells.remove(0)

print(shells)

