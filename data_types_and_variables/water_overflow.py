tank_capacity = 255
number_of_lines = int(input())
current_capacity = 0

new_capacity = 0

for i in range(number_of_lines):

    liters_of_water = int(input())

    if current_capacity <= tank_capacity:
        current_capacity += liters_of_water

        if current_capacity > tank_capacity:
            current_capacity -=liters_of_water
            print("Insufficient capacity!")

        else:
            new_capacity = current_capacity

print(new_capacity)