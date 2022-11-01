def loading_bar(number):
    if number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    percent_counter = 0
    dot_counter = 0
    percent_in_num = number // 10
    for current_percent in range(1, 11):
        if current_percent <= percent_in_num:
            percent_counter += 1
        else:
            dot_counter += 1
    return f"""{number}% [{percent_counter * "%"}{dot_counter* "."}]\nStill loading..."""



percent_number = int(input())
print(loading_bar(percent_number))