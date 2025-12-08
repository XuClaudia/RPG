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
        
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if player_type == "Finn" :
            weapon_list = weapon_list_Finn = ["Pocket knife", "Sword", "Katana"]
        elif player_type == "Ice_king":
            weapon_list = weapon_list_Ice_king = ["Snow ball", "icicle", "Gunter"]
        elif player_type == "Three_trunks" :
            weapon_list = weapon_list_Three_trunks = ["Spoon", "Rock", "Apple pie"]



        #self.weapon_type = random.choice(weapon_list)
        self.weapon_type = weapon_list[1]
        ### ik geef nu aan alle wapens op plek 1 dezelfde damage en plaats twee enz.
        if self.weapon_type == weapon_list[1]:
            self.min_damage = self.item_level * 2
            self.max_damage = self.item_level * 3
        
        elif self.weapon_type == weapon_list[2]:
            self.min_damage= 3
            self.max_damage = self.item_level * 4

        elif self.weapon_type == weapon_list[3]:
            self.min_damage = 5
            self.max_damage = self.item_level * 6
###~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
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
        

