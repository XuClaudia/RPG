class Item:
    inventory = []
    item_type = None
    
    def __init__(self, item_level):
        self.item_level = item_level
        
    def print_stats(self):
        print(self.item_type, "- level:", self.item_level)
        
import random

class Weapon(Item):
    def __init__(self, item_level, player_name):
        Item.__init__(self, item_level)
        
        self.item_type = "Weapon"
        
        if player_name == "Finn" :
            weapon_list = ["Pocket knife", "Sword", "Katana"]
        elif player_name == "Ice king":
            weapon_list = ["Snow ball", "icicle", "Gunter"]
        elif player_name == "Three trunks" :
            weapon_list = ["Spoon", "Rock", "Apple pie"]

        self.weapon_type = weapon_list[0]
        inventory.append(self.weapon_type)
        
        ### ik geef nu aan alle wapens op plek 1 dezelfde damage
        if self.weapon_type == weapon_list[0]:
            self.min_damage = self.item_level * 2
            self.max_damage = self.item_level * 3
        
        elif self.weapon_type == weapon_list[1]:
            self.min_damage= 3
            self.max_damage = self.item_level * 4

        elif self.weapon_type == weapon_list[2]:
            self.min_damage = 5
            self.max_damage = self.item_level * 6

    def print_stats(self):
        Item.print_stats(self)
        print(self.weapon_type, "damage:", self.min_damage, "-", self.max_damage)
            
class Armor(Item):
    def __init__(self, item_level):
        Item.__init__(self, item_level)
        self.item_type = "Armor"
        armor_list = ["leather", "brigandine", "Plate mail"]
        if level = 1:
         self.armor_type = armor_type[0]
        elif level = 2:
            self.armor_type = armor_type[1]
        elif level 3:
            self.armor_type = armor_type[2]
            
        self.defence = self.item_level * 2
        
    def print_stats(self):
        Item.print_stats(self)
        print("Defence:", self.defence)
        




