# Import the random library to use for the dice later
import random

# Define Variables
numLives = 10           # number of player's lives remaining
mNumLives = 12          # number of monster's lives remaining

diceOptions = list(range(1, 7))

#iterating through the weapons list
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear Bomb"]
print("Available weapons: ")
for weapon in range(len(weapons)):
    print(f"{weapon + 1}.{weapons[weapon]}")

while True:
    try:
        combatStrength = int(input("Enter your combat Strength (1-6): "))
        if 1 <= combatStrength <= 6:
            break
        else:
            print("Input must be an integer between 1-6")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")

while True:
    try:
        mcombatStrength = int(input("Enter the monster's combat Strength (1-6): "))
        if 1 <= mcombatStrength <= 6:
            break
        else:
            print("Input must be an integer between 1-6")
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")

#starting the battle
for i in range(1, 20, 2):
    #rolling the dice
    heroRoll = random.choice(diceOptions)
    monsterRoll = random.choice(diceOptions)

    #determining strength
    heroStrength = combatStrength + heroRoll
    monsterStrength = combatStrength + monsterRoll

    #determining weapons
    heroWeapon = weapons[heroRoll -1]
    monsterWeapon = weapons[monsterRoll -1]

    print(f"Round {i}: Hero rolled {heroRoll}, Monster rolled {monsterRoll}.")
    print(f"Hero selected: {heroWeapon}, Monster selected: {monsterWeapon}.")
    print(f"Hero Total Strength: {heroStrength}, Monster Total Strength: {monsterStrength}.")

    if heroStrength > monsterStrength:
        print("Hero wins the round!")
    elif heroStrength < monsterStrength:
        print("Monster wins the round!")
    else:
        print("It's a tie!")

    # Break condition for round 11
    if i == 11:
        print("\nBattle Truce declared in Round 11. Game Over!")
        break

