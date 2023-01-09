high = range(81, 126)
medium = range(51, 81)
low = range(1, 51)

fire_with_cells = input().split("#")
water = int(input())
lst_of_numbers = []
total_fire = 0
final_list = []
effort = 0


for numbers in fire_with_cells:

    lst_of_numbers = numbers.split("=")
    lst_of_numbers[-1] = int(lst_of_numbers[-1])

    if ("High" in numbers) and (lst_of_numbers[-1] in high) \
    or ("Medium" in numbers) and (lst_of_numbers[-1] in medium)\
    or ("Low" in numbers) and (lst_of_numbers[-1] in low):
        if water >= lst_of_numbers[-1]:
            water -= lst_of_numbers[-1]
            current_effort = 0.25 * lst_of_numbers[-1]
            total_fire += lst_of_numbers[-1]
            final_list.append(lst_of_numbers[-1])
            effort += current_effort

print("Cells:")
for current_fire in range(len(final_list)):
    print("-", final_list[current_fire])

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
