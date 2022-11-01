line_one = input().split(" ")
line_two = input().split(" ")
line_three = input().split(" ")
flag_win = False

if (line_one[0] == line_two[1] and line_two[1]== line_three[2]) or ((line_one[2] == line_two[1]) and (line_two[1] == line_three[0])) !=0:
    if line_two[1] == "1":
        print("First player won")
        flag_win = True
    elif line_two[1] == "2":
        print("Second player won")
        flag_win = True


for i in range(0, 3):
    if (line_one[i] == line_two[i] and line_two[i] == line_three[i]) != 0:
        if line_one[i] == "1":
            print("First player won")
            flag_win = True
        elif line_one[i] == "2":
            print("Second player won")
            flag_win = True

if (line_one[0] == line_one[1] and line_one[1] == line_one[2]) != 0:
    if line_one[i] == "1":
        print("First player won")
        flag_win = True
    elif line_one[i] == "2":
        print("Second player won")
        flag_win = True

elif (line_two[0] == line_two[1] and line_two[1] == line_two[2]) != 0:
        if line_two[0] == "1":
             print("First player won")
             flag_win = True
        elif line_two[0] == "2":
            print("Second player won")
            flag_win = True

elif (line_three[0] == line_three[1] and line_three[1] == line_three[2]) != 0:
        if line_three[0] == "1":
             print("First player won")
             flag_win = True
        elif line_three[0] == "2":
            print("Second player won")
            flag_win = True

if flag_win == False:
    print("Draw!")