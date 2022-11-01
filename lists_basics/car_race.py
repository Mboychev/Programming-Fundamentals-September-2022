sequence_of_times = input().split(" ")
time_left_int = []
time_right_int = []
total_time_left = 0
total_time_right = 0

middle = len(sequence_of_times)//2

left_racer_times = sequence_of_times[:middle]
right_racer_times = sequence_of_times[:middle:-1]

for current_time_left in left_racer_times:
    time_left_int.append(int(current_time_left))

for current_time_left_int in time_left_int:
    if current_time_left_int == 0:
        total_time_left *= 0.8
    else:
        total_time_left += current_time_left_int

for current_time_right in right_racer_times:
    time_right_int.append(int(current_time_right))

for current_time_right_int in time_right_int:
    if current_time_right_int == 0:
        total_time_right *= 0.8
    else:
        total_time_right += current_time_right_int

if total_time_left < total_time_right:
    print(f"The winner is left with total time: {total_time_left:.1f}")
else:
    print(f"The winner is right with total time: {total_time_right:.1f}")