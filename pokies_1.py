import random

# Symbols for slots
symbols = ["7", "💎", "🍋", "🍒", "🍀", "🎲"]

# Set starting balance for player
balance = 100
playing = True 

# Print welcome statement and balance
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
        continue # Let them try a smaller bet instead of quitting
    
    # Subtract spin cost
    balance -= spin_cost
    
    # Create empty 2d list 3x3
    slot_machine = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""]
    ]

    # Pick and place symbols 
    for row in range(3):
        for col in range(3):
            slot_machine[row][col] = random.choice(symbols)

    # Show results to the user
    print("\n--- SPINNING ---")
    for row in slot_machine:
        print(f"| {row[0]} | {row[1]} | {row[2]} |")

    # Win check logic
    won = False
    for row in slot_machine:
        if row[0] == row[1] == row[2]:
            winnings = spin_cost * 10
            balance += winnings
            print(f"JACKPOT! You matched {row[0]}! You won ${winnings}!")
            won = True
            
    # Output statement after spin 
    if not won:
        print("No match this time :(")

    print(f"Total Balance: ${balance}")

    # Ask to play again
    choice = input("\nWould you like to spin again? (y/n): ").lower()
    if choice != 'y':
        playing = False
        print(f"Thanks for playing! You're leaving with ${balance}")
       
