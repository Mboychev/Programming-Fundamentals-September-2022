


working_days_events = input().split("|")
total_energy = 100
total_coins = 100
day_completed = True

for current_event in working_days_events:
    splitted = current_event.split("-")
    event_order, event_number = splitted[0], int(splitted[1])


    if event_order == "rest":
        current_energy = total_energy
        total_energy += event_number
        if total_energy > 100:
            total_energy = 100
        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")



    elif  event_order == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coins += event_number
            print(f"You earned {event_number} coins.")

        else:
            total_energy += 50
            print("You had to rest!")


    else:

        if event_number <= total_coins:
            total_coins -= event_number
            print(f"You bought {event_order}.")


        else:
            day_completed = False
            print(f"Closed! Cannot afford {event_order}.")
            break

if day_completed:

    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")

