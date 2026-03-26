# TF 27/03/2026
# pokies.py

import random

# Symbols for slots
symbols = ["7", "💎", "🍋", "🍒", "🍀", "🎲"]

# Set starting balance for player
balance = 100
playing = True 

# --- FUNCTIONS ---

def check_win(line):
    return line[0] == line[1] == line[2]


def process_spin(slot_machine, spin_cost, balance):
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
    print("\n--- SPINNING ---")
    for row in grid:
        print(f"| {row[0]} | {row[1]} | {row[2]} |")


# --- GAME START ---

print("--- Welcome to the Pokies! ---")
print(f"You are starting with ${balance} credits")

while playing:
    # Ask for the bet first
    try:
        spin_cost = float(input(f"Your balance is ${balance} \nHow much would you like to bet? $"))
        if spin_cost <= 0:
            print("Please enter a bet greater than 0.")
            continue
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    
    # Check if user has enough money
    if balance < spin_cost:
        print(f"\nInsufficient balance! You need ${spin_cost} but only have ${balance}.")
        continue
    
    # Subtract spin cost
    balance -= spin_cost

    # generate + display BEFORE processing
    slot_machine = generate_grid(symbols)
    display_grid(slot_machine)

    # Process results
    balance, won = process_spin(slot_machine, spin_cost, balance)
            
    # Output statement for loss
    if not won:
        print("No match this time :(")

    print(f"Total Balance: ${balance}")

    # Ask to play again
    choice = input("\nWould you like to spin again? (y/n): ").lower()
    if choice != 'y':
        playing = False
        print(f"Thanks for playing! You're leaving with ${balance}")
