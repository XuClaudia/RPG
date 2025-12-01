class Monster:
    hp = 1
    max_hp = 1
    min_damage = 1
    max_damage = 1
    monster_type = None
    xp_value = 1
    
    def __init__(self, level):
        self.level = level
        
    def attack(self):
        damage = random.randint(self.min_damage, self.max_damage)
        print(self.monster_type, "attacks for", damage, "damage")
        return damage
    
    def take_hit(self, damage):
        self.hp -= damage
        if self.hp > 0:
            print(self.monster_type, "has", self.hp, "hp left")
        else:
            print(self.monster_type, "is slain")
            
    def print_stats(self):
        print(self.monster_type, "- level", self.level)
        if self.hp> 0:
            print("HP:", self.hp, "/", self.max_hp)
        else:
            print(self.monster_type, "defeated")

import random

class Skeleton(Monster):
    def __init__(self, level):
        Monster.__init__(self, level)
        
        self.monster_type = "Skeleton"
        self.hp = self.max_hp = self.level * 15
        self.min_damage = self.level + 1
        self.max_damage = self.level * 3
        self.xp_value = 100 + self.level * 20

class Troll(Monster):
    def __init__(self, level):
        Monster.__init__(self, level)
        
        self.monster_type = "Troll"
        self.hp = self.max_hp = self.level * 20
        self.min_damage = 1
        self.max_damage = self.level * 4
        self.xp_value = 100 + self.level * 20
        self.crit_chance = max(30, level * 10)
        
    def attack(self):
        damage = random.randint(self.min_damage, self.max_damage)
        #crit hit?
        if random.randint(1, 100) <= self.crit_chance:
            print(self.monster_type, "makes a critical hit!")
            damage *= 2
            
        print(self.monster_type, "attacks for", damage, "damage")
        return damage
