"""Loot and bonus gold helpers for the guild hall."""

import math
from .dice import roll


def split_loot(total, heroes): # This function calculates each hero's share of the total gold by dividing the total amount of gold by the number of heroes. It uses the math.ceil function to round up the result to the nearest whole number, ensuring that each hero receives at least one whole unit of gold. The function returns the calculated share as an integer.
    """Return each hero's share of the gold, rounded up."""
    return math.ceil(total / heroes)

def bonus_gold(): # This function generates a random bonus amount of gold by rolling a six-sided die (d6) and multiplying the result by 10. It uses the roll function from the dice module to simulate the die roll. The function returns the calculated bonus gold as an integer.
    """Return a random bonus amount of gold."""
    return roll(6) * 10