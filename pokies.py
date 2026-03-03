# Toaiva Faafia
# Creating a Slot Machine

import random

# Symbols list for slots
symbols = ["7", "💎", "🍋", "🍒", "🍀", "🎲"]

# Set a variable to keep loop running
playing = True

# Print Welcome statement
print("--- Welcome to the Slot Machine! ---")

while playing:
    # --- Everthing below this is indented ---
    
    # Create empty 2d list
    slot_machine = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]

    # For each row index
    for r in range(3):
        # For each column index
        for c in range(3):
            # Pick and place
            slot_machine[r][c] = random.choice(symbols)

    # Show results to the user
    print("\n--- SPINNING ---")
    for row in slot_machine:
        print(f"| {row[0]} | {row[1]} | {row[2]} |")

    # --- WIN CHECK LOGIC ---
    won = False
    for row in slot_machine:
        # Check if all items in the row are the same
        if row[0] == row[1] == row[2]:
            print(f"JACKPOT! You matched {row[0]}!")
            won = True
    
    if not won:
        print("No match this time.")
    # -----------------------

    # Ask the user if they want to go again
    choice = input("\nWould you like to spin again? (y/n): ").lower()

    # Check the input
    if choice != 'y':
        playing = False
        print("Thanks for playing! Final results shown above.")
