gifts = input().split(" ")
COMMAND_OUT_OF_STOCK = "OutOfStock"
COMMAND_REQUIRED = "Required"
COMMAND_JUST_IN_CASE = "JustInCase"
out_of_stock = []
counter = 0
while True:

        command = input()

        if command == "No Money":
                break
        if COMMAND_OUT_OF_STOCK in command:
                out_of_stock = command.split(" ")
                for index, current_gift in enumerate(gifts):
                        if out_of_stock[1] == current_gift:
                                gifts[index] = "None"
        elif COMMAND_REQUIRED in command:
                out_of_stock = command.split(" ")
                number = int(out_of_stock[-1])
                if number < len(gifts):
                        for c_index, c_current_gift in enumerate(gifts):
                                if number == c_index:
                                        gifts[c_index] = out_of_stock[1]

        elif COMMAND_JUST_IN_CASE in command:
                out_of_stock = command.split(" ")
                for j_index, j_current_gift in enumerate(gifts):
                        gifts[-1] = out_of_stock[1]

for i in range(len(gifts)):
        if "None" in (gifts):
                gifts.remove("None")



print((" ").join(gifts))

#
# gift_list = input().split()
#
# while True:
#         command = input()
#         if command == "No Money":
#                 break
#         command_set = command.split(" ")
#         if command_set[0] == "OutOfStock":
#                 for index, gift in enumerate(gift_list):
#                         if gift == command_set[1]:
#                                 gift_list.remove(gift)
#                                 gift_list.insert(index, "None")
#         elif command_set[0] == "Required":
#                 if int(command_set[-1]) < len(gift_list):
#                         for c_index, c_current_gift in enumerate(gift_list):
#                                  if int(command_set[-1]) == c_index:
#                                         gift_list[c_index] = command_set[1]
#
#         elif command_set[0] == "JustInCase":
#                 gift_list.pop(-1)
#                 gift_list.append(command_set[1])
# while "None" in gift_list:
#         gift_list.remove("None")
#
# print(" ".join(gift_list))