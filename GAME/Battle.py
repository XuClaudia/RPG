##regel 113

from Item import Item, Weapon, Armor
from Monster import Monster, Zombie, Candy, Vampire, Jelly, Evil_eyes, Goo_skulls
from Shop import Shop
from Player import Player
from SaveGame import save_game
import Locations
import Ascii
import random
import time


def text_effect(text):
    for letter in text:
        print(letter, end="")
        time.sleep(0.01)
        
class Battle:
    def __init__(self, player, current_location_name="Unknown"):
        self.player = player #link naar player
        self.current_location_name = current_location_name 
        self.difficulty = random.randint(1,3) #naar aantal monsters
        self.monster_list = []
        self.xp_value = 0
        self.gold_value = 0
        monster_type = ["Zombie", "Candy", "Vampire", "Jelly", "Evil_eyes", "Goo_skulls"]
        
        for i in range(self.difficulty): #monsters maken
            monster_choice = random.choice(monster_type)
            if monster_choice == "Zombie":
                self.monster_list.append(Zombie(self.player.level))
            elif monster_choice == "Candy":
                self.monster_list.append(Candy(self.player.level))
            elif monster_choice == "Vampire":
                self.monster_list.append(Vampire(self.player.level))
            elif monster_choice == "Jelly":
                self.monster_list.append(Jelly(self.player.level))
            elif monster_choice == "Evil_eyes":
                self.monster_list.append(Evil_eyes(self.player.level))
            elif monster_choice == "Goo_skulls":
                self.monster_list.append(Goo_skulls(self.player.level))
            
                
            self.xp_value += self.monster_list[i].xp_value
            self.gold_value += self.monster_list[i].gold_value
        
    def battle_stats(self):
        print("You are fighting:")
        print()
        
        for i in range(self.difficulty):
            print("Enemy", i + 1)
            self.monster_list[i].print_stats()
            print()
            
        print("\n" + "-"*75)
        print()

    def generate_loot(self): #new armor? buit
        #items genereren
        loot = False
        if self.difficulty == 1:
            if random.randint(1, 100) <= 25:
                loot = True
                
        elif self.difficulty == 2:
            if random.randint(1,100) <= 40:
                loot = True
        elif self.difficulty == 3:
            if random.randint(1,100) <= 60:
                loot = True
                
        if loot == True:
            #genereer een item voor player
            loot_list = ["Weapon", "Armor"]
            loot_type = random.choice(loot_list)
            
            if loot_type == "Weapon":
                item = Weapon(random.randint(self.player.level, self.player.level + 1), self.player.name)
                print("Yay, the monsters dropped a new weapon")
            elif loot_type == "Armor":
                item = Armor(random.randint(self.player.level, self.player.level + 1))
                print("Yay, the monsters dropped new armor")

            item.print_stats()
            print()
            print("Your current stats are:")
            self.player.print_stats()
            print()
            
            choice = input("Do you want to equip the new item? (Y/N)").upper()
            choice = choice.lower()
            
            if choice == "n":
                print("You leave the item on the ground and move on...")
            else:
                self.player.equip_item(item)
                print("You equiped the new item.")
        
        else:
            #geen buit gevonden
            print("You found no equip")
            #player.print_stats()
             
            
    def monster_attack(self):
        for monster in self.monster_list:
            if monster.hp <= 0:
                continue
            # Zombie effect: weapon verzwakken
            if isinstance(monster, Zombie):     #van hier tot r. 126 (monster.sugar_effect(self.player)) is gemaakt m.b.v. AI\
                print("Whwuuuubuuu whwuuubuu BRAINS.\nI will destroy your WEAPON!")
                print("Before:", self.player.weapon.min_damage, "-", self.player.weapon.max_damage)
                    
                 # Verlaag weapon damage
                self.player.weapon.min_damage = max(1, self.player.weapon.min_damage - 1)
                self.player.weapon.max_damage = max(
                     self.player.weapon.min_damage,
                    self.player.weapon.max_damage // 2
                )

                print("After:", self.player.weapon.min_damage, "-", self.player.weapon.max_damage)
                print()
            
            # Gewone damage van de zombie (of andere monsters)
            monster_damage = monster.attack()
            self.player.take_hit(monster_damage)
            
       #Als het een Candy is, voer sugar effect uit     
            if isinstance(monster, Candy):
                monster.sugar_effect(self.player)
            
       #Als het een evil_eyes is dan voert die zijn effect uit.     
            if isinstance(monster, Evil_eyes):
                monster.verzwak_armor(self.player)
    
    def player_attack(self):
        #monsters zijn genummerd
        #speler valt die aan
        if self.player.skip_attack:
            print("🍬 You are too dizzy to attack this round!")
            self.player.skip_attack = False
            return
        
        if len(self.monster_list)> 1: #aantal monsters
            max_target = len(self.monster_list)
            target = -1
            while target < 1 or target > max_target:
                try:
                    target = int(input("Which monster would you like to attack? ( 1 - " + str(max_target) + ")"))
                except ValueError:
                    print("Please enter a valid number!")
            target -= 1
        else:
            target = 0 #plek nul in de lijst monster 1
            
        monster = self.monster_list[target]
            
        #Strijdkreetjes van de monsters
        if isinstance (monster, Zombie):
           # print("Whwuuuubuuu whwuuubuu BRAINS.\n")
           # time.sleep(1)
           # print("I will destroy your WEAPON\n")

            self.player.weapon.print_stats()
           # print("--->")
           # original_max = self.player.weapon.max_damage
            #self.player.weapon.min_damage = max(1, self.player.weapon.min_damage - 1)
            #self.player.weapon.max_damage = max(self.player.weapon.min_damage, int(original_max * 0.75))
            #self.player.weapon.print_stats()
            #time.sleep(2)
            
        elif isinstance (monster, Candy):
            text_effect("My taste may be sweet BUT\n")
            time.sleep(0.5)
            text_effect("Too much of me will effect you.\n")
            
        elif isinstance (monster, Vampire):
            text_effect("Hello there!\n") 
            time.sleep(1)
            text_effect("I smell the scent of your blood\n")
            
        elif isinstance (monster, Jelly):
            text_effect("The Jelly starts wobbling uncontrollably...\n")
                
        elif isinstance(monster, Evil_eyes):
            text_effect("The Evil Eyes lock onto you...\n")
            time.sleep(0.6)
            text_effect("They see every weakness in your armor.\n")
   
        elif isinstance (monster, Goo_skulls):
            text_effect("You will die just like ME MUHAHAHAHAHA\n")

        player_damage = self.player.attack()
        if self.monster_list[target].hp > 0: #als de monster nog leeft hp> 0 
#             self.monster_list[target].take_hit(player_damage) #krijgt monster damage van player
            
            if isinstance(monster, Jelly):
                monster.take_hit(player_damage, self.player)
            else:
                monster.take_hit(player_damage)
                
        else:
            print("You hit the dead monster, it is still dead...\n")
    
    def player_heal(self):
        if random.randint(1,100) <= 40:
            heal_amount = (random.randint(self.player.max_hp // 4, self.player.max_hp //3))
            self.player.heal(heal_amount)
        else:
            print("You tried to heal yourself, it failed...")
            
    def player_run(self):
        if random.randint(1, 100) <= 25:
            print("You ran away as fast as you could and you lost the monsters")
            return True
        else:
            print("You failed to run")
            return False
    
    def player_quit(self):
        print("You gave up......?")
        self.player.hp = 0
    
    def fight_battle(self): #game loop
        time.sleep(1)
        
        while True:
            self.player.skip_attack = False  #Zodat als er meer dan 1 candy is, wordt de speler niet steeds geblokkeerd.
            print()
            Ascii.display_art("Battle round")
            #print("\n" + "###" + " BATTLE ROUND " + "#"*60)
            self.battle_stats()
            
            not_has_shop = False  # default
            for location in Locations.LOCATIONS:
                if location["name"] == self.current_location_name:
                    not_has_shop = location.get("has_shop", False)
                    break
                
            if not_has_shop:
                player_action = " "
                while player_action not in ["S","F","H","R", "O", "V", "Q"]:
                    player_action = input("What will you do? (S)tats, (F)ight, (H)eal, (R)un, sh(O)p, sa(V)e, (Q)uit").upper()
                    print()
            else:
                player_action = " "
                while player_action not in ["S","F","H","R", "V", "Q"]:
                    player_action = input("What will you do? (S)tats, (F)ight, (H)eal, (R)un, sa(V)e, (Q)uit").upper()
                    print()
            
            if player_action == "S":
                self.player.print_stats()
                input("[PRESS ENTER TO CONTINUE THE BATTLE]")
                
            elif player_action == "F":
                self.player_attack()
                monsters_alive = 0
                for monster in self.monster_list:
                    if monster.hp > 0:
                        monsters_alive += 1
                 
                if monsters_alive > 0:
                    self.monster_attack()
                    
                else:
                    print()
                    print("\n" + "#"*90)
                    print( "####" + "  YOU WON ✧⁺⸜(･ ᗜ ･ )⸝⁺✧  " +"#"*60)
                    print("#"*90)
                    
                    self.player.xp_gain(self.xp_value)
                    self.player.gold_gain(self.gold_value)
                    self.generate_loot()
                    input("[PRESS ENTER TO CONTINUE]")
                    self.player.level += 1
                    break
                
            elif player_action == "H":
                self.player_heal()
                print()
                self.monster_attack()
                
            elif player_action == "R":
                if  self.player_run() == True:
                    break
                else:
                    self.monster_attack()
                    
            elif player_action == "O":
                    shop = Shop(self.player)
                    shop.shop_loop()
                
            elif player_action == "V":
                save_game(self.player)    
                    
            elif player_action == "Q":
                self.player_quit()
                break
            
            if self.player.hp <= 0:
                print("\n" + "#"*82)
                print("\n" + "!"*82)
                print("\n" + "!!!" + " You are dead " +"!"*65)
                print("\n" + "!"*82)
                print("\n" + "#"*82)
                 
                break
                




