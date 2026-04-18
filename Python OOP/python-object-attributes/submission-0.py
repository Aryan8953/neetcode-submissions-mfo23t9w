class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name
        self.species = species
        self.hunger = hunger
        self.energy = energy

whiskers = Pet("Whiskers", "cat", 6, 8)

print(f"Initial Attributes: {whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")

# 2. Modify Whiskers' attributes
whiskers.hunger -= 3
whiskers.energy += 2

# 3. Print Whiskers' modified attributes
print(f"Modified Attributes: {whiskers.name} ({whiskers.species}) - Hunger: {whiskers.hunger}, Energy: {whiskers.energy}")
