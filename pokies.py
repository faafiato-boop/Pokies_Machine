# Toaiva Faafia
# Creating a Slot Machine

import random

# Symbols list for slots
symbols = ["7", "💎", "🍋", "🍒", "🍀", "🎲"]

# Welcome user statement
print("--- Welcome to the Slot Machine! ---")

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

# Show results to the user️
for row in slot_machine:
    
    # Print one horizontal row at a time
    print(row) 
