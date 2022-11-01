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