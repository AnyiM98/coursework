from characters.py import Character

class Player(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon

    def attack(self, other):
        damage = 10
        print(f"{self.name} attacks {other.name} with {self.weapon} for {damage} damage.")
        other.health -= damage
