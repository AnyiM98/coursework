class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def attack(self, other):
        pass

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} (Health: {self.health})"
