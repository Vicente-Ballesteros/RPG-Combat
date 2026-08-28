from character import Character

class Enemy(Character):
    def __init__(self, name, health, attack, defence, weapon):
        super().__init__(name, health, attack, defence, weapon)