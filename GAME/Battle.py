from Item import Item, Weapon, Armor
from Monster import Monster, Vampire, Goo_Skulls
import random

class Battle:
    def __init__(self, player):
        self.player = player #link naar palyer
        self.difficulty = random.randint(1,3) #naar aantal monsters
        self.monster_list = []
        self.xp_value = 0
        monster_type = ["Vampire", "Goo_Skulls"]
        
        for i in range(self.difficulty): #monsters maken
            monster_choice = random.choice(monster_type)
            if monster_choice == "Vampire":
                self.monster_list.append(Vampire(self.player.level))
            elif monster_choice == "Goo_Skulls":
                self.monster_list.append(Goo_Skulls(self.player.level))
                
            self.xp_value += self.monster_list[i].xp_value
            
    def battle_stats(self):
        print("You are fighting:")
        
        for i in range(self.difficulty):
            print("Enemy", i + 1)
            self.monster_list[i].print_stats()
            print()
            
        print("###################################################################################")
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
                item = Weapon(random.randint(self.player.level, self.player.level + 1))
                print("YAy, the monsters dropped new weapon")
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
            
            
            
            
    def monster_attack(self):
        for monster in self.monster_list:
            if monster.hp >0:
                monster_damage = monster.attack()
                self.player.take_hit(monster_damage)
    
    def player_attack(self):
        #monsters zijn genummerd
        #speler valt die aan
        if len(self.monster_list)> 1: #aantal monsters
            max_target = len(self.monster_list)
            target = -1
            while target < 1 or target > max_target:
                target = int(input("Which monster would you like to attack? ( 1 -" + str(max_target) + ")"))
            target -= 1
        else:
            target = 0 #plek nul in de lijst monster 1
            
        player_damage = self.player.attack()
        if self.monster_list[target].hp > 0:
            self.monster_list[target].take_hit(player_damage)
        else:
            print("You hit the dead monster, it is still dead...")
    
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
        print("You are under attack")
        
        while True:
            print()
            print("####### BATTLE ROUND ##############################################################")
            print()
            self.battle_stats()
            
            player_action = " "
            while player_action not in ["S","F","H","R", "Q"]:
                player_action = input("What will you do? (S)tats, (F)ight, (H)eal, (R)un, (Q)uit").upper()
                print()
            
            if player_action == "S":
                self.player.print_stats()
                input("Press enter to continue the fight")
                
            elif player_action == "F":
                self.player_attack()
                monsters_alive = 0
                for monster in self.monster_list:
                    if monster.hp > 0:
                        monsters_alive += 1
                 
                if monsters_alive > 0:
                    self.monster_attack()
                    
                else:
                    print("###########################################################################################################")
                    print("####### You won ###########################################################################################")
                    print("###########################################################################################################")
                    
                    self.player.xp_gain(self.xp_value)
                    self.generate_loot()
                    input("Press enter to continue")
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
                    
            elif player_action == "Q":
                self.player_quit()
                break
            
            if self.player.hp <= 0:
                print("############################")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("!!!!!!!!!!!You are dead!!!!!!!!!!!!!!!!!!!!!!")
                print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
                print("############################")
                 
                break
                

            

