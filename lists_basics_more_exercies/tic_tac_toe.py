"""You will receive a field of a tic-tac-toe game in three lines containing numbers, separated by a single space.
Legend:
•	0 - empty space
•	1 - first player move
•	2 - second player move
Find out who the winner is. If the first player wins, print "First player won". If the second player wins, print
"Second player won". Otherwise, print "Draw!".
###################################EXAMPLES#######################################
Input:
2 0 1
0 1 0
1 0 2
Output: First player won

Input:
0 1 0
2 2 2
1 0 0
Output: Second player won

Input:
1 0 2
0 1 2
1 2 0

Output: Draw! """
line_one = input().split(" ")
line_two = input().split(" ")
line_three = input().split(" ")
flag_win = False

if (line_one[0] == line_two[1] and line_two[1] == line_three[2]) \
        or ((line_one[2] == line_two[1]) and (line_two[1] == line_three[0])) !=0:
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

if not flag_win:
    print("Draw!")