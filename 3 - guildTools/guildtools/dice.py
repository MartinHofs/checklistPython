"""guildtools.dice - Dice helpers for the guild hall."""

# dice.roll(sides)
#   What it does: One random roll from 1 to sides (the random module).
#   Returns: A whole number
# dice.roll_many(count, sides)
#   What it does: A list of count random rolls from 1 to sides (the random module).
#   Returns: A list of whole numbers

import random


def roll(sides): # This function simulates rolling a single die with a specified number of sides. It uses the random module to generate a random integer between 1 and the number of sides (inclusive). The function returns the result of the die roll as an integer.
    """Return one random roll from 1 to sides."""
    return random.randint(1, sides)

def roll_many(count, sides): # This function simulates rolling multiple dice with a specified number of sides. It takes two parameters: count (the number of dice to roll) and sides (the number of sides on each die). The function uses a list comprehension to generate a list of random integers, each representing the result of a die roll. It returns a list containing the results of all the rolls.
    """Return a list of count random rolls from 1 to sides."""
    return [roll(sides) for _ in range(count)]