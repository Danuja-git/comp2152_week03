# Sample Coding Questions Week 02
# Name: Danuja Shankar

import random

# Array of weapons
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

try:
    # Roll the dice
    weaponRoll = random.randint(1, 6)  # Rolling a dice (1-6)
    print(f"You rolled: {weaponRoll}")

    # Add to hero's combat strength (example: combat_strength = 10)
    hero_combat_strength = 10
    hero_combat_strength += weaponRoll
    print(f"Hero's combat strength: {hero_combat_strength}")

    # Use the roll as an index and print the weapon
    weapon = weapons[weaponRoll - 1]  # Index is roll - 1
    print(f"Hero's weapon: {weapon}")

    # Check the condition
    if weaponRoll <= 2:
        print("You rolled a weak weapon, friend.")
    elif weaponRoll <= 4:
        print("Your weapon is meh.")
    else:
        print("Nice weapon, friend!")

    # Additional condition
    if weapon != "Fist":
        print("Thank goodness you didn't roll the Fist...")

except ValueError:
    print("Error: Invalid input detected. Please ensure input is an integer.")
