"""Write a program that announces the winner of a car race.
You will receive a sequence of numbers. Each number represents the time the car needs to pass through that step
(the index). There will be two cars. The first one starts from the left side, and the other one starts from the
right side. The middle index of the sequence is the finish line.
Calculate the total time each racer needs to reach the finish line and print the winner with his total time
(the racer with less time). If you have a zero in the list, you should reduce the racer's time that reached
it by 20% (from his current time).
The number of elements in the sequence will always be odd.
Print the result in the following format "The winner is {left/right} with total time: {total_time}".
The time should be formatted to the first decimal point.
###################################EXAMPLES#######################################
Input: 29 13 9 0 13 0 21 0 14 82 12
Output: The winner is left with total time: 53.8

Input: 123 20 4 0 13 0 0 5 5 14 0
Output: The winner is right with total time: 19.2"""

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