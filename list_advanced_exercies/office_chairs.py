"""You are a facility manager at a large business center. One of your responsibilities is to check if each conference
room in the center has enough chairs for the visitors.
On the first line, you will be given an integer n representing the number of rooms in the business center.
On the following n lines for each room, you will receive information about the chairs in the room and the number of
visitors. Each chair will be presented with the char "X". Next, there will be a single space and the number of visitors
at the end. For example: "XXXXX 4" (5 chairs and 4 visitors).
Keep track of the free chairs:
•	If there are not enough chairs in a specific room, print the following message: "{needed_chairs_in_room} more chairs
needed in room {number_of_room}". The rooms start from 1.
•	Otherwise, print: "Game On, {total_free_chairs} free chairs left".
###################################EXAMPLES#######################################
Input:
4
XXXX 4
XX 1
XXXXXX 3
XXX 3
Output: Game On, 4 free chairs left

Input:
3
XXXXXXX 5
XXXX 5
XXXXXX 8
Output:
1 more chairs needed in room 2
2 more chairs needed in room 3
"""

# def chair_check(rooms):
#     chairs_left = 0
#     chairs_needed = 0
#
#     chairs, visitors = input().split()
#     difference = len(chairs) - int(visitors)
#     if difference >= 0:
#         chairs_left += difference
#     else:
#         chairs_needed += difference
#
#     return chairs_left, chairs_needed
#
#
# number_of_rooms = int(input())
# total_left = 0
# total_needed = 0
#
#
# for current_room in range(1, number_of_rooms + 1):
#     left, needed = chair_check(number_of_rooms)
#     if needed < 0:
#         print(f"{abs(needed)} more chairs needed in room {current_room}")
#         total_needed += needed
#     else:
#         total_left += left
#
# if total_left >= abs(total_needed):
#     print(f"Game On, {total_left} free chairs left")
#
#
#
#
def chair_check(rooms):
    chairs_left = 0
    chairs_needed = 0

    for current_room in range(1, rooms + 1):
        chairs, people = input().split()
        difference = len(chairs) - int(people)

        if difference >= 0:
            chairs_left += difference
        else:
            chairs_needed += abs(difference)
            print(f"{abs(difference)} more chairs needed in room {current_room}")

    return chairs_left, chairs_needed


number_of_rooms = int(input())
total_chairs_left, total_chairs_needed = chair_check(number_of_rooms)

if total_chairs_left >= total_chairs_needed:
    print(f"Game On, {total_chairs_left} free chairs left")