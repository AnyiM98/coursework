import random
from player import Player
from enemies import Goblin, Troll

class Game:
    def __init__(self, player):
        self.player = player
        self.enemies = [Goblin(), Troll()]

    def play(self):
        print("Starting game...")
        while self.player.is_alive() and self.enemies:
            enemy = random.choice(self.enemies)
            print(f"A wild {enemy.name} appears!")
            while enemy.is_alive() and self.player.is_alive():
                self.player.attack(enemy)
                if enemy.is_alive():
                    enemy.attack(self.player)
            if not enemy.is_alive():
                print(f"{enemy.name} is defeated!")
                self.enemies.remove(enemy)
            if not self.player.is_alive():
                print("You have been defeated. Game over.")
        if self.player.is_alive():
            print("Congratulations! You have defeated all enemies.")
        else:
            print("You have been defeated. Game over.")
