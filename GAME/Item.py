class Item:
    item_type = None
    
    def __init__(self, item_level):
        self.item_level = item_level
        
    def print_stats(self):
        print(self.item_type, "- level:", self.item_level)
        
import random

class Weapon(Item):
    def __init__(self, item_level):
        Item.__init__(self, item_level)
        
        self.item_type = "Weapon"
        weapon_list =["Sword", "Axe"]
        self.weapon_type = random.choice(weapon_list)
        if self.weapon_type == "Sword":
            self.min_damage = self.item_level * 2
            self.max_damage = self.item_level * 3
        
        elif self.weapon_type == "Axe":
            self.min_damage= 1
            self.max_damage = self.item_level * 4
            
    def print_stats(self):
        Item.print_stats(self)
        print(self.weapon_type, "damage:", self.min_damage, "-", self.max_damage)
            
class Armor(Item):
    def __init__(self, item_level):
        Item.__init__(self, item_level)
        self.item_type = "Armor"
        self.defence = self.item_level * 2
        
    def print_stats(self):
        Item.print_stats(self)
        print("Defence:", self.defence)
        
