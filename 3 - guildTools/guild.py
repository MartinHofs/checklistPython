import sys

from guildtools.dice import roll, roll_many
from guildtools.loot import split_loot, bonus_gold


COMMANDS = {
    "roll": roll,
    "split": split_loot,
    "today": lambda: __import__("datetime").date.today(),
    "bonus": bonus_gold,
}
USAGE = "Usage: python guild.py roll SIDES | split TOTAL HEROES | today | bonus"

# Format:
    # $ python guild.py roll 20
    # Rolled a d20: 10
    # $ python guild.py split 100 3
    # Each of 3 heroes gets 34 gold.
    # $ python guild.py today
    # Today is 2026-11-23.
    # $ python guild.py dance
    # Usage: python guild.py roll SIDES | split TOTAL HEROES | today
    # $ python guild.py 
    # Usage: python guild.py roll SIDES | split TOTAL HEROES | today

    # $ python -m pydoc guildtools.dice
    # Help on module guildtools.dice in guildtools:

    # NAME
    #     guildtools.dice - Dice helpers for the guild hall.

    # FUNCTIONS
    #     roll(sides)
    #         Return one random roll from 1 to sides.
        
    #     roll_many(count, sides)
    #         Return a list of count rolls of a die with the given sides.

def main():
    if len(sys.argv) < 2:
        print(USAGE)
        return

    command = sys.argv[1]
    if command not in COMMANDS:
        print(USAGE)
        return

    try:
        args = [int(arg) for arg in sys.argv[2:]]
    except ValueError:
        print(USAGE)
        return

    result = COMMANDS[command](*args)
    if command == "roll":
        print(f"Rolled a d{args[0]}: {result}")
    elif command == "split":
        print(f"Each of {args[1]} heroes gets {result} gold.")
    elif command == "today":
        print(f"Today is {result}.")
    elif command == "bonus":
        print(f"Bonus gold: {result}")

if __name__ == "__main__":
    main()