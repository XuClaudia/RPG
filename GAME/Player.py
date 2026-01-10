from Item import Item, Weapon, Armor
import random
import time

def text_effect(text):
    for letter in text:
        print(letter, end="")
        time.sleep(0.01)

class Player:
    
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.xp = 0
        self.next_level_xp = 500
        self.hp = 50
        self.max_hp = 50
        self.gold = 10
        self.weapon = Weapon (1, name)
        self.armor = Armor(1)
        self.has_grenade = False
        self.skip_attack = False

    
    def attack(self):
        damage = self.level + random.randint(self.weapon.min_damage, self.weapon.max_damage)
        if self.has_grenade:
            damage += 20
            self.has_grenade = False
            print(f"💥 {self.name} throws a GRENADE for {damage} damage!")
        else:
            print(self.name, "attacks with a", self.weapon.weapon_type, "for", damage, "damage")
        return damage
    
        
    def take_hit(self, damage):
        final_damage = damage - self.armor.defence
        if final_damage> 0:
            self.hp -= final_damage
            if self.hp <= 0:
                print("AAAAAAAAAAAAAAa! You died!")
                time.sleep(1)
            else:
                print("ouch! You take", final_damage, "damage!")
                print("You have", self.hp, "hitpoints left!")
                time.sleep(1)
                #input("[PRESS ENTER TO CONTINUE]")
    
        else:
            #geen damage/ afgeweerd
            print("Your shiny armor protects you: You take no damage!")
            time.sleep(1)
        
        
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
           
            if self.level == 2:
                self.weapon = Weapon(self.level, self.name)
                print("Your weapon has been upgraded!")
            elif self.level == 3:
                self.weapon = Weapon(self.level, self.name)
                print("Your weapon has reached its final form!")
            
                
            self.print_stats()
            
    def gold_gain(self, gold_amount):
        self.gold += gold_amount
        print("You have gained ", gold_amount, "gold!.")
        
        
    def equip_item(self, item):
        if item.item_type == "Weapon":
            self.weapon = item
        elif item.item_type == "Armor":
            self.armor = item
            
        self.print_stats()
    
    
    
    def print_stats(self):
        print("="*90)
        print("  Name: " + self.name)
        print("  Level: " + str(self.level) )
        print("  HP: " + str(self.hp) + "/" + str(self.max_hp))
        print("  XP: " + str(self.xp) + "/" + str(self.next_level_xp))
        print("  Gold: " + str(self.gold))
        print("-"*90 )
        self.weapon.print_stats()
        self.armor.print_stats()
        print("="*90)


