import random, time
class Monster:
    hp = 1
    max_hp = 1
    min_damage = 1
    max_damage = 1
    monster_type = None
    xp_value = 1
    
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
        print("Whwuuuubuuu whwuuubuu BRAINS.") 
        time.sleep(1)
        print ("I will destroy your WEAPON")

        self.monster_type = "Zombie"
        self.hp = self.max_hp = self.level * 10
        self.min_damage = self.weapon.min_damage - 1    # De weapon damage van de speler wordt met één verlaagd en zo dus ook verlaagd.
        self.max_damage = self.weapon.max_damage // 2    #De weapon damage van de speler wordt gehalveerd en zo dus verlaagd.
        self.xp_value = 100 + self.level * 25
        
class Candy(Monster):
    def __init__(self, level):
        Monster.__init__(self, level)
        print("My taste may be sweet BUT")
        time.sleep(0.5)
        print("Too much of me will effect you.")  

        self.monster_type = "Candy"
        self.hp = self.max_hp = self.level * 5
        self.min_damage = self.level + 2
        self.max_damage = self.level + 4


class Vampire(Monster):                         
    def __init__(self, level):
        Monster.__init__(self, level)
        print("Hello there!") 
        time.sleep(1)
        print("I smell the scent of your blood")
        
        self.monster_type = "Vampire"
        self.hp = self.max_hp = self.level * 15
        self.min_damage = self.level + 1
        self.max_damage = self.level * 3
        self.xp_value = 100 + self.level * 20

class Goo_Skulls(Monster):
    def __init__(self, level):
        Monster.__init__(self, level)
        print("You will die just like ME MUHAHAHAHAHA")
        
        self.monster_type = "Goo_Skulls"
        self.hp = self.max_hp = self.level * 20
        self.min_damage = 1
        self.max_damage = self.level * 4
        self.xp_value = 100 + self.level * 20
        self.crit_chance = max(30, level * 10)
        
    def attack(self):
        damage = random.randint(self.min_damage, self.max_damage)
        #crit hit?
        if random.randint(1, 100) <= self.crit_chance:
            print(self.monster_type, "makes a critical hit!")
            damage *= 2
            
        print(self.monster_type, "attacks for", damage, "damage")
        return damage





