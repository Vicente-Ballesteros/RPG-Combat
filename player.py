from character import Character

class Player(Character):
    def __init__(self, name, health, attack, defence, weapon):
        super().__init__(name, health, attack, defence, weapon)