from characters import Character

class Enemy(Character):
    def __init__(self, name, health, strength):
        super().__init__(name, health)
        self.strength = strength

    def attack(self, other):
        print(f"{self.name} attacks {other.name} with strength {self.strength}.")
        other.health -= self.strength

class Goblin(Enemy):
    def __init__(self):
        super().__init__("Goblin", 30, 5)

class Troll(Enemy):
    def __init__(self):
        super().__init__("Troll", 50, 15)
