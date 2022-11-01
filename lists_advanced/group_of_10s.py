data = input()
data_int = [int(x) for x in data.split(", ")]

max_value = 10
group_counter = 0

while len(data_int) > 0:

    current_group = []

    for index, value in enumerate(data_int):
        if value <= max_value:
            current_group.append(value)
            data_int.pop(index)
            data_int.insert(index, 0)

    for number in range(len(data_int)):
        if 0 in data_int:
            data_int.remove(0)
    max_value += 10
    group_counter += 10
    print(f"Group of {group_counter}'s: {current_group}")

