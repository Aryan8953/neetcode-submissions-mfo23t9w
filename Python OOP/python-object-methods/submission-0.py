class Pet:
    def __init__(self, name: str):
        self.name = name
        self.hunger = 5

    def feed(self):
        self.hunger -= 1
        # 2. Print the feeding message
        print(f'{self.name} has been fed.')
        # 3. Print the current hunger level
        print(f"{self.name}'s hunger level: {self.hunger}")
        pass

# Create a pet
my_pet = Pet("Fluffy")

# TODO: Feed the pet three times
my_pet.feed()
my_pet.feed()
my_pet.feed()