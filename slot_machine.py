"""pokies.py."""
# TF 1/04/2026


# Import random module so slot machine randomly chooses symbols
import random

# Minimum required for VIP status
VIP_THRESHOLD = 500

# Symbols for slots
symbols = ["7", "💎", "🍋", "🍒", "🍀", "🎲"]


# --- FUNCTIONS ---
def check_win(line):
    """Check if all 3 symbols in a row match."""
    return line[0] == line[1] == line[2]


def process_spin(slot_machine, spin_cost, player_profile):
    """Process the spin result and calculate any winnings."""
    total_winnings = 0
    won = False

    # Checks each row is in slot_machine
    for row in slot_machine:
        # If all symbols in the row match, calculate and award winnings
        if check_win(row):
            winnings = round(spin_cost * 10, 2)     # learnt this skill from gemini, rounds to 2d.p
            total_winnings += winnings
            print(f"JACKPOT! You matched {row[0]}! You won ${winnings}!")
            won = True

    player_profile["balance"] += total_winnings
    return player_profile, won


def generate_grid(symbols):
    """Generate 3x3 grid with random symbols."""
    grid = [["", "", ""], ["", "", ""], ["", "", ""]]

    # Fill each position with a random symbol
    for row in range(3):
        for col in range(3):
            grid[row][col] = random.choice(symbols)

    return grid


def display_grid(grid):
    """Display pokies in formatted layout."""
    print("\n--- SPINNING ---")

    # Loop through each row and display symbols
    for row in grid:
        print(f"| {row[0]} | {row[1]} | {row[2]} |")


def ask_play_again():
    """Prompt layer to choose whether to spin slot machine again."""
    # Keep asking until 'y' or 'n' is entered
    while True: 
        choice = input("\nWould you like to spin again? (y/n): ").lower()

        # Return true if player wants to continue
        if choice == 'y':
            return True

        # Return false if player wants to stop
        elif choice == 'n':
            return False

        # Handle invalid input and prompt again
        else:
            print("Invalid input. Please enter 'y' or 'n'.")


def check_marketing_status(player_profile):
    """Check player's losses and enable promotional targeting if entitled."""

    # If player exceeds $500 
    if player_profile["lifetime_losses"] > VIP_THRESHOLD: 
        print("\n💰 VIP OFFER UNLOCKED! 💰")
        print("Double your next deposit! Buy more credits now!")
        player_profile["target_ads"] = True

    # Show encouragement and disable ads
    else:
        print("\nKeep playing to climb the leaderboard!")
        player_profile["target_ads"] = False


def get_starting_balance():
    """Robust input for starting deposit."""
    # Keep prompting until a valid starting deposit is entered
    while True: 
        # Get user input and convert it to a decimal number
        try:
            amount = float(input("Enter your starting deposit: $"))

            # Ensure deposit is greater than zero
            if amount <= 0:
                print("Deposit must be greater than 0.")
                # Restart loop for invalid amount
                continue 

            return round(amount, 2)
        
        # Handle cases where input is not a valid number
        except ValueError:
            print("Invalid input. Please enter a valid number.")


# Main game loop
def main():
    """Go over main function."""
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

    # Continue running the game until the player quits or runs out of money 
    while playing:
        # Stop if no money left
        if player_profile["balance"] <= 0:
            print("\nSorry, you're out of money!")
            break

        # --- BET INPUT ---
        
        # Keep asking player for a bet amount until valid input is entered
        # Ask how much user wants to bet
        try:
            spin_cost = float(input("How much would you like to bet? $"))
                
            # Ensure the bet amount is greater than zero
            if spin_cost <= 0:
                print("Please enter a bet greater than 0.")
                break
            # Prevent betting more than the available balance
            if spin_cost > player_profile["balance"]:
                print("Insufficient balance!")
                break
            # Round the bet amount to two decimal places
            spin_cost = round(spin_cost, 2)

            # Handle invalid numeric input from the user
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
