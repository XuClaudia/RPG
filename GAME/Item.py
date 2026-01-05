import time

def text_effect(text):
    for letter in text:
        print(letter, end="")
        time.sleep(0.01)
        
class Item:
    inventory = []
    item_type = None
    
    def __init__(self, item_level):
        self.item_level = item_level
        
    def print_stats(self):
        text_effect(self.item_type + " - level: " ) #+ str(self.item_level)
        
import random

class Weapon(Item):
    def __init__(self, item_level, player_name, weapon_name = None):
        Item.__init__(self, item_level)
        
        self.item_type = "Weapon"
        
        if weapon_name:
            self.weapon_type = weapon_name #als de naam in de shop al was gegeven
        elif player_name == "Finn" :
            weapon_list = ["Pocket_knife", "Sword", "Katana"]
        elif player_name == "Ice king":
            weapon_list = ["Snowball", "icicle", "Gunter"]
        elif player_name == "Tree trunks" :
            weapon_list = ["Spoon", "Rock", "Applepie"]

        self.weapon_list = weapon_list
        self.weapon_type = weapon_list[0]
        self.set_damage()
       
    def set_damage(self):
        ### ik geef nu aan alle wapens op plek 1 dezelfde damage
        if self.weapon_type == self.weapon_list[0]:
            self.min_damage = self.item_level * 2
            self.max_damage = self.item_level * 3
        
        elif self.weapon_type == self.weapon_list[1]:
            self.min_damage=  self.item_level * 3
            self.max_damage = self.item_level * 4

        elif self.weapon_type == self.weapon_list[2]:
            self.min_damage =  self.item_level * 4
            self.max_damage = self.item_level * 5
            
        elif self.weapon_type == "Dragon_sword": #shop
            self.min_damage =  self.item_level * 6
            self.max_damage = self.item_level * 8
            
        elif self.weapon_type == "Fork": #shop
            self.min_damage =  self.item_level * 5
            self.max_damage = self.item_level * 8
            
    def upgrade_damage(self, upgrade_amount): #shop
        self.min_damage += upgrade_amount
        self.max_damage += upgrade_amount
        print("⚡ Weapon upgraded! Damage: " + self.min_damage + " - " + self.max_damage)

    def print_stats(self):
        Item.print_stats(self)
        print(self.weapon_type + "_damage: " + str(self.min_damage) + "-" + str(self.max_damage) + "\n")
            
class Armor(Item):
    def __init__(self, item_level):
        Item.__init__(self, item_level)
        self.item_type = "Armor"
        armor_list = ["leather", "brigandine", "plate_mail"]
        self.armor_type = ""
        self.armor_type = random.choice(armor_list)
        self.defence = 1
        if self.armor_type == "leather":
            self.defence = self.item_level * 2
        elif self.armor_type == "brigandine":
            self.defence = self.item_level * 3
        elif self.armor_type == "plate_mail":
            self.defence = self.item_level * 4
            
         
    def print_stats(self):
        Item.print_stats(self)
        print(self.armor_type + "_defence:" + str(self.defence) + "\n")
        

