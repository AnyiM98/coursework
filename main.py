from player import Player
from game import Game

def main():
    name = input("Enter your character's name: ")
    player = Player(name, 100, "sword")
    game = Game(player)
    game.play()

if __name__ == "__main__":
    main()
