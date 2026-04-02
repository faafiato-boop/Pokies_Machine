# TF 1/04/2026
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

    # Check each row for win and add jackpot if won
    for row in slot_machine:
        if check_win(row):
            winnings = spin_cost * 10
            total_winnings += winnings
            print(f"JACKPOT! You matched {row[0]}! You won ${winnings}!")
            won = True

    # adding winnings and return updated balance
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

    # Fill 3x3 grid with random symbols
    for row in range(3):
        for col in range(3):
            grid[row][col] = random.choice(symbols)

    return grid


def display_grid(grid):
    """
    Print the 3x3 grid to the console with formatting.
    """
    print("\n--- SPINNING ---")

    # Print each row of the grid pokies style
    for row in grid:
        print(f"| {row[0]} | {row[1]} | {row[2]} |")


def ask_play_again():
    """
    Ask the user if they want to play again.
    Only accepts 'y' or 'n'.
    """

    # Continuously prompt the user until they enter 'y' or 'n'
    # Returning True for yes (spin again) and False for no
    while True:
        choice = input("\nWould you like to spin again? (y/n): ").lower()

        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def main():
    """
    Run the main game loop for the slot machine.
    """
    balance = 100
    playing = True

    print("--- Welcome to the Pokies! ---")

    # --- MAIN GAME LOOP ---
    while playing:  # Loop continues as long as the player wants to spin
        # Continuously prompt for a valid bet
        while True:  # Inner loop handles input validation
            try:
                spin_cost = float(input(f"Your balance is ${balance} \nHow much would you like to bet? $"))

                if spin_cost <= 0:  # Ensure bet is positive
                    print("Please enter a bet greater than 0.")
                    continue

                if spin_cost > balance:  # Ensure player has enough money
                    print(f"Insufficient balance! You need ${spin_cost} but only have ${balance}.")
                    continue

                break  # Valid bet entered, exit input loop

            except ValueError:  # Handle invalid input
                print("Invalid input. Please enter a number.")

        # --- SPIN THE SLOT MACHINE ---
        slot_machine = generate_grid(symbols)  # Generate a new 3x3 grid
        display_grid(slot_machine)  # Display the slot machine

        balance -= spin_cost  # Deduct the bet from the balance

        # Process the spin and update balance
        balance, won = process_spin(slot_machine, spin_cost, balance)

        # Display message when no winning combination is found
        if not won:
            print("No match this time :(")

        #print updated balance after spin
        print(f"Your new balance is: ${balance}")
            

        # Ask to play again
        playing = ask_play_again()


if __name__ == "__main__":
    main()
