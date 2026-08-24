import random

class Character:
    def __init__(self, name, health, attack, defence):
        self.name = name
        self.health = health
        self.attack = attack
        self.is_alive = True
        self.defence = defence

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.is_alive = False

    def attack_enemy(self, enemy):
        enemy.take_damage(self.attack)

hero1 = Character("Aragorn", 100, 20)
hero2 = Character("Legolas", 90, 15)

while hero1.is_alive and hero2.is_alive:
    hero1.attack_enemy(hero2)
    if not hero2.is_alive:
        print(f"{hero2.name} has been defeated!")
        break
    hero2.attack_enemy(hero1)
    if not hero1.is_alive:
        print(f"{hero1.name} has been defeated!")
        break


