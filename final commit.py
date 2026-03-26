# TF 27/03/2026
# pokies.py

import random

# Symbols for slots
symbols = ["7", "💎", "🍋", "🍒", "🍀", "🎲"]

# --- FUNCTIONS ---

def check_win(line):
    """
    Return True if all three symbols in the list match.
    """
    return line[0] == line[1] == line[2]


def process_spin(slot_machine, spin_cost, balance):
    """
    Calculate winnings based on matching rows and update the balance.
    """
    total_winnings = 0
    won = False

    for row in slot_machine:
        if check_win(row):
            winnings = spin_cost * 10
            total_winnings += winnings
            print(f"JACKPOT! You matched {row[0]}! You won ${winnings}!")
            won = True

    balance += total_winnings
    return balance, won


def generate_grid(symbols):
    """
    Generate a 3x3 grid of random symbols from the provided list.
    """
    grid = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]

    for row in range(3):
        for col in range(3):
            grid[row][col] = random.choice(symbols)

    return grid


def display_grid(grid):
    """
    Print the 3x3 grid to the console with formatting.
    """
    print("\n--- SPINNING ---")
    for row in grid:
        print(f"| {row[0]} | {row[1]} | {row[2]} |")


def main():
    """
    Run the main game loop for the slot machine.
    """
    balance = 100
    playing = True

    print("--- Welcome to the Pokies! ---")

    while playing:
        try:
            spin_cost = float(input(f"Your balance is ${balance} \nHow much would you like to bet? $"))
            if spin_cost <= 0:
                print("Please enter a bet greater than 0.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if balance < spin_cost:
            print(f"\nInsufficient balance! You need ${spin_cost} but only have ${balance}.")
            continue
        
        balance -= spin_cost

        slot_machine = generate_grid(symbols)
        display_grid(slot_machine)

        balance, won = process_spin(slot_machine, spin_cost, balance)
                
        if not won:
            print("No match this time :(")

        print(f"Total Balance: ${balance}")

        choice = input("\nWould you like to spin again? (y/n): ").lower()
        if choice != 'y':
            playing = False
            print(f"Thanks for playing! You're leaving with ${balance}")


if __name__ == "__main__":
    main()
