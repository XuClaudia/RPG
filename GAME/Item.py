import time

def text_effect(text):
    for letter in text:
        print(letter, end="")
        time.sleep(0.05)
        
class Item:
    inventory = []
    item_type = None
    
    def __init__(self, item_level):
        self.item_level = item_level
        
    def print_stats(self):
        text_effect(self.item_type + " - level: " ) #+ str(self.item_level)
        
import random

class Weapon(Item):
    def __init__(self, item_level, player_name):
        Item.__init__(self, item_level)
        
        self.item_type = "Weapon"
        
        if player_name == "Finn" :
            weapon_list = ["Pocket_knife", "Sword", "Katana"]
        elif player_name == "Ice king":
            weapon_list = ["Snowball", "icicle", "Gunter"]
        elif player_name == "Three trunks" :
            weapon_list = ["Spoon", "Rock", "Applepie"]

        self.weapon_type = weapon_list[0]
        Item.inventory.append(self.weapon_type)
        
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
        text_effect(self.weapon_type + "damage: " + str(self.min_damage) + "-" + str(self.max_damage) + "\n")
            
class Armor(Item):
    def __init__(self, item_level):
        Item.__init__(self, item_level)
        self.item_type = "Armor"
        armor_list = ["leather", "brigandine", "plate_mail"]
        self.armor_type = ""
        self.armor_type == random.choice(armor_list)
        self.defence = 1
        if self.armor_type == "leather":
            self.defence = self.item_level * 2
        elif self.armor_type == "brigandine":
            self.defence = self.item_level * 3
        elif self.armor_type == "plate_mail":
            self.defence = self.item_level * 4
            
         
    def print_stats(self):
        Item.print_stats(self)
        text_effect(self.armor_type + "defence:" + str(self.defence) + "\n")
        




