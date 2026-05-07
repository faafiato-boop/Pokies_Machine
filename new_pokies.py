# TF 1/04/2026
# pokies.py

# Imports random module so slot machine randomly chooses symbols
import random

# Symbols for slots
symbols = ["7", "💎", "🍋", "🍒", "🍀", "🎲"]

# --- FUNCTIONS ---

def check_win(line):
    """
    Checks if all 3 symbols in a row match
    """
    return line[0] == line[1] == line[2]


def process_spin(slot_machine, spin_cost, player_profile):
    """
    Processes the spin result and calculates any winnings
    """
    total_winnings = 0
    won = False

    # Checks each row is in slot_machine
    for row in slot_machine:
        
        if check_win(row):
            winnings = round(spin_cost * 10, 2) 
            total_winnings += winnings
            print(f"JACKPOT! You matched {row[0]}! You won ${winnings}!")
            won = True

    player_profile["balance"] += total_winnings
    return player_profile, won


def generate_grid(symbols):
    grid = [["", "", ""], ["", "", ""], ["", "", ""]]

    for row in range(3):
        for col in range(3):
            grid[row][col] = random.choice(symbols)

    return grid


def display_grid(grid):
    print("\n--- SPINNING ---")
    for row in grid:
        print(f"| {row[0]} | {row[1]} | {row[2]} |")


def ask_play_again():
    while True:
        choice = input("\nWould you like to spin again? (y/n): ").lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def check_marketing_status(player_profile):
    if player_profile["lifetime_losses"] > 500:
        print("\n💰 VIP OFFER UNLOCKED! 💰")
        print("Double your next deposit! Buy more credits now!")
        player_profile["target_ads"] = True
    else:
        print("\nKeep playing to climb the leaderboard!")
        player_profile["target_ads"] = False  


def get_starting_balance():
    """Robust input for starting deposit"""
    while True:
        try:
            amount = float(input("Enter your starting deposit: $"))

            if amount <= 0:
                print("Deposit must be greater than 0.")
                continue

            return round(amount, 2)

        except ValueError:
            print("Invalid input. Please enter a valid number.")


def main():
    print("\n--- Welcome to the Pokies! ---")
    
    # Player setup
    player_profile = {
        "name": input("Enter your name: "),
        "location": input("Enter your location: "),
        "high_score": 0,
        "lifetime_losses": 0,
        "balance": get_starting_balance(),
        "target_ads": False
    }

    playing = True

    while playing:
        # Stop if no money left
        if player_profile["balance"] <= 0:
            print("\nSorry, you're out of money!")
            break

        # --- BET INPUT ---
        while True:
            try:
                spin_cost = float(input(
                    f"How much would you like to bet? $"
                ))

                if spin_cost <= 0:
                    print("Please enter a bet greater than 0.")
                    continue

                if spin_cost > player_profile["balance"]:
                    print("Insufficient balance!")
                    continue

                spin_cost = round(spin_cost, 2)
                break

            except ValueError:
                print("Invalid input. Please enter a number.")

        # --- SPIN ---
        slot_machine = generate_grid(symbols)
        display_grid(slot_machine)

        # Deduct bet
        player_profile["balance"] -= spin_cost

        # Process result
        player_profile, won = process_spin(slot_machine, spin_cost, player_profile)

        # Tracking losses
        if not won:
            print("No match this time :(")
            player_profile["lifetime_losses"] += spin_cost

        # Update high score (as integer)
        if player_profile["balance"] > player_profile["high_score"]:
            player_profile["high_score"] = int(player_profile["balance"])  

        # Marketing check
        check_marketing_status(player_profile)

        # Display stats
        print(f"\nPlayer: {player_profile['name']} ({player_profile['location']})")
        print(f"Balance: ${player_profile['balance']}")
        print(f"High Score: ${player_profile['high_score']}")
        print(f"Lifetime Losses: ${player_profile['lifetime_losses']}")

        # Play again
        playing = ask_play_again()


if __name__ == "__main__":
    main()
