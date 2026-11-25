import sys

from guildtools.dice import roll, roll_many
from guildtools.loot import split_loot, bonus_gold


COMMANDS = {
    "roll": roll,
    "split": split_loot,
    "today": lambda: __import__("datetime").date.today(),
    "bonus": bonus_gold,
} # The commands dictionary maps command names to their corresponding functions.
USAGE = "Usage: python guild.py roll SIDES | split TOTAL HEROES | today | bonus" #The usage string provides instructions on how to use the script, including the available commands and their expected arguments.

def main(): # The main function serves as the entry point for the script. It processes command-line arguments, validates them, and executes the corresponding command based on user input.
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