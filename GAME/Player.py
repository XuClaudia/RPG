from Item import Item, Weapon, Armor
import random
import time

def text_effect(text):
    for letter in text:
        print(letter, end="")
        time.sleep(0.01)

class Player:
    level = 1
    xp = 0
    next_level_xp = 500
    hp = 50
    max_hp = 50
    
    def __init__(self, name):
        self.name = name
        self.weapon = Weapon (1, name)
        self.armor = Armor (1)


    
    def attack(self):
        damage = self.level + random.randint(self.weapon.min_damage, self.weapon.max_damage)
        print(self.name, "attacks with a", self.weapon.weapon_type, "for", damage, "damage")
        return damage
    
        
    def take_hit(self, damage):
        final_damage = damage - self.armor.defence
        if final_damage> 0:
            self.hp -= final_damage
            if self.hp <= 0:
                print("AAAAAAAAAAAAAAa! You died!")
            else:
                print("ouch! You take", final_damage, "damage!")
                print("You have", self.hp, "hitpoints left!")
    
        else:
            #geen damage/ afgeweerd
            print("Your shiny armor protects you: You take no damage!")
            
    def heal(self, heal_amount):
        self.hp += heal_amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp
            
        print("You healed for", heal_amount, "hp.")
        print("You currently have ", self.hp, "/", self.max_hp, "hp.")
    
    def xp_gain(self, xp_amount):
        self.xp += xp_amount
        print("You have gained ", xp_amount, "xp!.")
        
        #level up
        if self.xp >= self.next_level_xp:
            self.level += 1
            self.xp -=self.next_level_xp
            
            self.next_level_xp = int(self.next_level_xp * 1.25)
            self.max_hp = int(self.max_hp * 1.2)
            self.hp = self.max_hp
           
            if self.level == 1:
                #wordt level 2
                self.weapon_type = weapon_list[1]
                print("YAYYY! You have reached level", self.level, "!")
            elif self.level == 2:
                #wordt level 3
                self.weapon_type = weapon_list[2]
                print("YAYYY! You have reached level", self.level, "!")
            elif self.level == 3:
                print("You have reach the FINAL BATTLE")
                print("You now get the chance to level up your weapon")
                #dit kan later een item shop worden
                ##############
                self.weapon_type = weapon_list[2]
                y = input(int("Choose a number between 1 and 5"))
                self.max_damage = self.item_level * y
                
                #wapen blijft het zelfde, maar krijgt nu de mogelijkheid om beter te worden
            
                
            self.print_stats()
    
    def equip_item(self, item):
        if item.item_type == "weapon":
            self.weapon = item
        elif item.item_type == "armor":
            self.armor = item
            
        self.print_stats()
    
    
    
    def print_stats(self):
        print()
        
        print("###################################################################################")
        print("#######" + self.name + " stats: ######################################################")
        print("###################################################################################")
        text_effect("  Name: " + self.name + "\n")
        text_effect("  Level: " + str(self.level) + "\n")
        text_effect("  HP: " + str(self.hp) + "/" + str(self.max_hp) + "\n")
        text_effect("  XP: " + str(self.xp) + "/" + str(self.next_level_xp) + "\n")
        print("-----------------------------------------------------------------------------------\n")
        self.weapon.print_stats()
        self.armor.print_stats()
        print("###########################################\n")

        
        
        
            

