wagons = int(input())

train = wagons * [0]

while True:

    command = input().split(" ")

    current_command = command[0]

    if current_command == "End":
        break

    elif current_command == "add":
        train[-1] += int(command[1])

    elif current_command == "insert":
        train[int(command[1])] += int(command[-1])

    elif current_command == "leave":
        train[int(command[1])] -= int(command[-1])

print(train)