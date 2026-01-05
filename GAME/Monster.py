#let op toegevoegde gold_value
import random, time
class Monster:
    hp = 1
    max_hp = 1
    min_damage = 1
    max_damage = 1
    monster_type = None
    xp_value = 1
    gold_value = 1
    
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
    #--------------------------------Verschillende soorten monsters -----------------------------------------
# Spelertype 1: Ice king(Archer) Spelertype 2: Finn(sword player) Spelertype 3: Tree Trunks (archer)
# Wapens voor type 1: a. Snowball b. Iceicle c. gunter(dingen gooien) Type 2: a. Pocket knife b. Finn's sword c. Katana Type: 3: a. spoon b. Rock c. Apple pie
# Monsters die tegenkomt: A. Zombie B. Candy C. vampire D. Jelly Cube E. Evil Eyes F. Goo skulls

class Zombie(Monster):                         #De zombie (monster) heeft als doel om de weapon damage van de speler te verlagen. 
    def __init__(self, level):
        Monster.__init__(self, level)
        self.monster_type = "Zombie"
        self.hp = self.max_hp = self.level * 10
        #code is geplaatst naar Battle +- regel 111
        #self.min_damage = self.weapon.min_damage - 1    # De weapon damage van de speler wordt met één verlaagd en zo dus ook verlaagd.
        #self.max_damage = self.weapon.max_damage // 2    #De weapon damage van de speler wordt gehalveerd en zo dus verlaagd.
        self.xp_value = 100 + self.level * 25
        self.gold_value = 5 + self.level * 50
        
class Candy(Monster):                     #De candy(monster) zorgt ervoor dat de speler een kans heeft om niet meer aan te vallen bij een ronde. 
    def __init__(self, level):
        Monster.__init__(self, level) 
        self.monster_type = "Candy"
        self.hp = self.max_hp = self.level * 5
        self.min_damage = self.level + 2
        self.max_damage = self.level + 4
        self.xp_value = 100 + self.level * 25
        self.gold_value = 5 + self.level * 50


        
class Vampire(Monster):                         
    def __init__(self, level):
        Monster.__init__(self, level)
        self.monster_type = "Vampire"
        self.hp = self.max_hp = self.level * 15
        self.min_damage = self.level + 1
        self.max_damage = self.level * 3
        self.xp_value = 100 + self.level * 20
        self.gold_value = 5 + self.level * 50

class Jelly(Monster):
    def __init__(self, level):
        Monster.__init__(self, level)
        self.monster_type = "Jelly"


class Evil_eyes(Monster):
    def __init__(self, level):
        Monster.__init__(self, level)

        self.monster_type = "Evil_eyes"


class Goo_skulls(Monster):
    def __init__(self, level):
        Monster.__init__(self, level)   
        self.monster_type = "Goo_skulls"
        self.hp = self.max_hp = self.level * 20
        self.min_damage = 1
        self.max_damage = self.level * 4
        self.xp_value = 100 + self.level * 20
        self.gold_value = 5 + self.level * 50
        self.crit_chance = max(30, level * 10)
        
    def attack(self):
        damage = random.randint(self.min_damage, self.max_damage)
        #crit hit?
        if random.randint(1, 100) <= self.crit_chance:
            print(self.monster_type, "makes a critical hit!")
            damage *= 2
            
        print(self.monster_type, "attacks for", damage, "damage")
        return damage

