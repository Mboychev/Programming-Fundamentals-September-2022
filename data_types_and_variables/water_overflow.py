"""You have a water tank with a capacity of 255 liters. On the first line, you will receive n – the number of lines,
which will follow. On the following n lines, you will receive liters of water (integers), which you should pour into
your tank. If the capacity is not enough, print "Insufficient capacity!" and continue reading the next line.
On the last line, print the liters in the tank.
###################################EXAMPLES#######################################
Input:
5
20
100
100
100
20

Output:
Insufficient capacity!
240

Input:
7
10
20
30
10
5
10
20

Output: 105

Input:
1
1000

Output:
Insufficient capacity!
0

Input:
4
250
10
20
40

Output:
Insufficient capacity!
Insufficient capacity!
Insufficient capacity!
250

"""

tank_capacity = 255
number_of_lines = int(input())
current_capacity = 0

new_capacity = 0

for i in range(number_of_lines):

    liters_of_water = int(input())

    if current_capacity <= tank_capacity:
        current_capacity += liters_of_water

        if current_capacity > tank_capacity:
            current_capacity -= liters_of_water
            print("Insufficient capacity!")

        else:
            new_capacity = current_capacity

print(new_capacity)