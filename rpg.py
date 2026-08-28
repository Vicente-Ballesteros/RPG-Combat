import random
from character import Character
from weapon import Weapon
from player import Player
from enemy import Enemy

weapon1 = Weapon("Sword", 0.8, 15)
weapon2 = Weapon("Bow", 0.9, 12)
hero1 = Player("Aragorn", 100, 20, 10, weapon1)
hero2 = Enemy("Legolas", 90, 15, 12, weapon2)

while hero1.is_alive and hero2.is_alive:
    hero1.attack_enemy(hero2)
    if not hero2.is_alive:
        print(f"{hero2.name} has been defeated!")
        break
    hero2.attack_enemy(hero1)
    if not hero1.is_alive:
        print(f"{hero1.name} has been defeated!")
        break

