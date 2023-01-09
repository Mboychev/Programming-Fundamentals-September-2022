# WHEN CHOOSING LINES, 1 STANDS FOR THE TOP ONE, 2 STANDS TOP AND MID AND 3 ARE ALL LINES.

import random

MIN_BET = 1
MAX_BET = 10000
MAX_LINES = 3

ROWS = 3
COLS = 3

symbols_to_play = {
    "💎": 3,
    "🌍": 10,
    "🌙": 15,
    "🌞": 30
}

values_multiplier = {
    "💎": 100,
    "🌍": 20,
    "🌙": 10,
    "🌞": 5
}


def check_play():
    while True:
        user_input = input(f"Would you like to play slots?(Yes/No): ")
        if user_input.lower() == "yes":
            return True
        elif user_input.lower() == 'no':
            return False
        else:
            print(f"Please enter a valid answer.")


def deposit():
    while True:
        deposit_amount = input(f"How much would you like to deposit?: ")
        if deposit_amount.isdigit():
            current_deposit = int(deposit_amount)
            if current_deposit > 0:
                break
            else:
                print(f"Amount must be greater than 0.")
        else:
            print(f"Please enter a valid number.")
    return current_deposit


def choose_lines():
    while True:
        how_many_lines = input(f"How many lines would you like to bet on?(1-{MAX_LINES}): ")
        if how_many_lines.isdigit():
            how_many_lines = int(how_many_lines)
            if 1 <= how_many_lines <= 3:
                break
            else:
                print(f"Lines must be a number between 1-{MAX_LINES}!")
        else:
            print(f"Please enter a valid number between 1-{MAX_LINES}!")
    return how_many_lines


def place_bet(current_balance):
    while True:
        print(f"Current balance: ${current_balance}")
        current_bet = input(f"How much money would you like to bet on each line?({MIN_BET} - {MAX_BET}): ")
        if current_bet.isdigit():
            current_bet = int(current_bet)
            if MIN_BET <= current_bet <= MAX_BET:
                break
            else:
                print(f"Please enter a valid number between ${MIN_BET} - ${MAX_BET}!")
        else:
            print(f"Please enter a valid number between ${MIN_BET} - ${MAX_BET}!")
    return current_bet


def spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(rows):
        all_symbols_copied = all_symbols[:]
        column = []
        for _ in range(cols):
            random_element = random.choice(all_symbols_copied)
            column.append(random_element)
            all_symbols_copied.remove(random_element)
        columns.append(column)

    return columns


def print_spin(cols):
    print("~~~~~~~~~~~~")
    for i in range(len(cols[0])):
        for symbol in cols[i]:
            print(symbol, end=" | ")
        print()
    print("~~~~~~~~~~~~")


def check_winnings(lines, columns, value, bet):
    winnings = 0
    for line in range(lines):
        winning_symbol = set()
        for symbol in columns[line]:
            winning_symbol.add(symbol)
        if len(winning_symbol) == 1:
            symbol = list(winning_symbol)[0]
            winnings += value[symbol] * bet
    return winnings


def press_enter_to_spin(bet, lines):
    total_bet = bet * lines
    print(f"You have bet ${total_bet} on {lines} lines.")
    current_spin = spin(ROWS, COLS, symbols_to_play)
    print(f"Spinning...")
    print_spin(current_spin)
    return check_winnings(lines, current_spin, values_multiplier, bet)


def change_lines_or_bet(current_balance):
    while True:
        user_input1 = f"What would you like to change?(bet/lines): "
        if user_input1 == "bet":
            changed_bet = place_bet(current_balance)
            return changed_bet, "lines"
        elif user_input1 == "lines":
            changed_lines = choose_lines()
            return changed_lines, "lines"
        else:
            print(f"Please enter a valid input.")


def no_money_left():
    while True:
        user_input = input(f"No money left! Would you like to deposit more?(Yes/No): ")
        if user_input.lower() == 'yes':
            main()
            break
        elif user_input.lower() == 'no':
            print(f"GoodBye! Do not gamble again!")
            exit()
        else:
            print(f"Please enter a valid input.")


def spin_again(balance, total_bet, bet, amount_lines):
    if balance >= total_bet:
        balance -= total_bet
        current_winnings = press_enter_to_spin(bet, amount_lines)
        if current_winnings > 0:
            balance += current_winnings
            print(f"YOU HAVE WON {current_winnings}!!!")
        else:
            print(f"You did not win :(")
        print(f"Balance remaining: ${balance}")
        return balance
    elif total_bet > balance:
        print(f"Not enough money to spin!")
        exit()


def changed(balance, amount_lines):
    while True:
        bet = place_bet(balance)
        total_bet = bet * amount_lines
        current_spin = spin(ROWS, COLS, symbols_to_play)
        check_winnings_var = check_winnings(amount_lines, current_spin, values_multiplier, bet)
        if total_bet > balance:
            print(f"Not enough money to spin!")
            break
        else:
            balance -= total_bet
            print(f"You have bet ${total_bet} on {amount_lines} lines.")
            print(f"balance left: ${balance}")
            print(f"Spinning...")
            print_spin(current_spin)
            break
    if check_winnings_var > 0:
        print(f"YOU HAVE WON ${check_winnings_var}!!!")
        return check_winnings_var, True, bet
    else:
        return f"You did not win :(", False, bet


def main():
    balance = deposit()
    amount_lines = choose_lines()

    while True:
        bet = place_bet(balance)
        total_bet = bet * amount_lines
        current_spin = spin(ROWS, COLS, symbols_to_play)
        check_winnings_var = check_winnings(amount_lines, current_spin, values_multiplier, bet)
        if total_bet > balance:
            print(f"You do not have that amount.")
        else:
            balance -= total_bet
            print(f"You have bet ${total_bet} on {amount_lines} lines.")
            print(f"Spinning...")
            print_spin(current_spin)
            break
    if check_winnings_var > 0:
        print(f"YOU HAVE WON ${check_winnings_var}!!!")
        balance += check_winnings_var
    else:
        print(f"You did not win :(")
    print(f"Current Balance: ${balance}")

    while True:
        if balance > 0:
            user_input = input(
                f"Press enter to spin the same bet and lines, 'c' to change bet and lines, and 'q' to leave.")

            if user_input == "":
                new_bal = spin_again(balance, total_bet, bet, amount_lines)
                balance = new_bal

            elif user_input == "c":
                while True:
                    user_input1 = input(f"What would you like to change?(Bet/Lines): ")
                    if user_input1.lower() == "bet":
                        bet = place_bet(balance)
                        total_bet = bet * amount_lines
                        new_bal = spin_again(balance, total_bet, bet, amount_lines)
                        balance = new_bal
                        break
                    elif user_input1.lower() == "lines":
                        amount_lines = choose_lines()
                        total_bet = bet * amount_lines
                        new_bal = spin_again(balance, total_bet, bet, amount_lines)
                        balance = new_bal
                        break
            elif user_input == 'q':
                print(f"Withdrawing...")
                print(f"Withdrawing Complete!")
                print(f"Goodbye!")
                break

        else:
            no_money_left()


if check_play():
    main()
else:
    print(f"GoodBye!")