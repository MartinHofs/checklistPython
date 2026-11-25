# classes and functions for the creature family
# Creature(name, health)
#   Base class. Stores name and health. Has the class attribute species = "creature".
#   Instance attributes: name, health
# Creature.attack()
#   Returns 1.	
# Creature.describe()
#   Returns NAME the SPECIES (HEALTH HP), for example Thing the creature (10 HP).	Uses self.species
# Creature.take_damage(amount)
#   Lowers health by amount. Health never goes below 0.	
# Creature.is_alive()
#   True when health is above 0.	
# Goblin(name)
#   Species "goblin". Health 20, set by calling super().__init__. attack() returns 4.	Constructor takes only a name
# Dragon(name)
#   Species "dragon".
#   Health 100 through super().__init__, plus a new attribute breath = "fire". attack() returns 20. describe() returns the base description plus , breathing fire.	describe calls super().describe()
# Slime(name)
#   Species "slime". Health 8 through super().__init__. Does not define attack, so the base attack of 1 is used.	
# total_attack(creatures)
#   What it Does: One loop over a list of mixed creatures, adding up each creature's attack(). Returns 0 for an empty list.
#   Results: A function, not a method

class Creature:
    species = "creature"

    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self):
        return 1

    def describe(self):
        return f"{self.name} the {self.species} ({self.health} HP)"

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)

    def is_alive(self):
        return self.health > 0

class Goblin(Creature):
    species = "goblin"

    def __init__(self, name):
        super().__init__(name, 20)

    def attack(self):
        return 4

class Dragon(Creature):
    species = "dragon"

    def __init__(self, name):
        super().__init__(name, 100)
        self.breath = "fire"

    def attack(self):
        return 20

    def describe(self):
        return super().describe() + f", breathing {self.breath}"

class Slime(Creature):
    species = "slime"

    def __init__(self, name):
        super().__init__(name, 8)

def total_attack(creatures):
    total = 0
    for creature in creatures:
        total += creature.attack()
    return total

# The demonstration in main()
# Build a party of two goblins, a dragon and a slime. Print each creature's description and attack, then the total attack, as in the sample run.
# Damage the dragon for 30, print its description again, and print a goblin's health to show that damage to one creature does not change another.
# End the file with the main guard.

def main():
    party = [
        Goblin("Grix"),
        Dragon("Smaug"),
        Slime("Blob"),
        Goblin("Snik")
    ]

    for creature in party:
        print(f"{creature.describe()} attacks for {creature.attack()}")

    print(f"Total attack: {total_attack(party)}")

    # Damage the dragon
    party[1].take_damage(30)
    print(party[1].describe())

    # Show that damage to one creature does not affect another
    print(f"{party[0].name}'s health unchanged: {party[0].health}")

if __name__ == "__main__":
    main()