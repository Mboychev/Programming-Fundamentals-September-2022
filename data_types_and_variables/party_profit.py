group_size = int(input())
days = int(input())
total_coins = 0
total_companions = group_size

for day in range(1, days + 1):


    if day % 15 == 0:
        total_companions += 5

    if day % 10 == 0:
        total_companions -= 2

    if day % 3 == 0:
        total_coins -= total_companions * 3

    if day % 5 == 0:
        total_coins += 20 * total_companions
        if day % 3 == 0:
            total_coins -= total_companions * 2

    total_coins += 50
    total_coins -= total_companions * 2

coins = int(total_coins / total_companions)

print(f"{total_companions} companions received {coins} coins each.")
