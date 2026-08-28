import random 

class Character:
    def __init__(self, name, health, attack, defence, weapon):
        self.name = name
        self.health = health
        self.attack = attack
        self.is_alive = True
        self.defence = defence
        self.weapon = weapon

    def take_damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.is_alive = False

    def does_hit(self, enemy):
        my_accuracy = self.attack + self.weapon.accuracy_bonus
        hit_chance = my_accuracy / (my_accuracy + enemy.defence)
        return random.random() < hit_chance

    def attack_enemy(self, enemy):
        if self.does_hit(enemy):
            damage = random.randint(1, self.weapon.max_hit)
            enemy.take_damage(damage)
            print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        else:
            print(f"{self.name}'s attack misses!")