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

# De zombie(monster) zorgt ervoor dat de weapon damage van de speler lager wordt. De bijbehorende overige code zit bij battle code onder def monster_attack +- r. 103
class Zombie(Monster):     
    def __init__(self, level):
        super().__init__(level)
        self.monster_type = "Zombie"
        self.hp = self.max_hp = level * 10
        self.min_damage = 1
        self.max_damage = 3
        self.xp_value = 100 + self.level * 25
        self.gold_value = 5 + self.level * 30

#De candy(monster) zorgt ervoor dat de speler een kans heeft om niet meer aan te vallen bij een ronde.        
class Candy(Monster):                      
    def __init__(self, level):
        Monster.__init__(self, level) 
        self.monster_type = "Candy"
        self.hp = self.max_hp = self.level * 25
        self.min_damage = self.level + 2
        self.max_damage = self.level + 3
        self.xp_value = 100 + self.level * 25
        self.gold_value = 5 + self.level * 50
        
    def sugar_effect(self, player):
        if player.skip_attack:
            return  # Zodat als er meer dan 1 candy is, wordt de speler niet steeds geblokkeerd.
        if random.randint(1, 100) <= 70:
            player.skip_attack = True
            print("🍬 You feel dizzy from the sugar rush!")
            print("🍬 You will miss your next attack!")


class Vampire(Monster):                         
    def __init__(self, level):
        Monster.__init__(self, level)
        self.monster_type = "Vampire"
        self.hp = self.max_hp = self.level * 15
        self.min_damage = self.level + 1
        self.max_damage = self.level * 3
        self.xp_value = 100 + self.level * 20
        self.gold_value = 5 + self.level * 20

#De Jelly(monster) zorgt ervoor dat de speler een aanval op zichzelf riskeert. De speler heeft 50% kans dat zijn eigen damage kapot gaat of er komt juist damage op de monster.
class Jelly(Monster):
    def __init__(self, level):
        Monster.__init__(self, level)
        self.monster_type = "Jelly"
        self.hp = self.max_hp = level * 15
        self.min_damage = self.level + 1
        self.max_damage = self.level * 4
        self.xp_value = 100 + self.level * 20
        self.gold_value = 5 + self.level * 55

    
    def take_hit(self, damage, player = None):
        print("The Jelly jiggles strangely... 🫧")
        
        if random.randint(1, 100) <= 50: # Dan is de aanval dus op de speler.
            print("😵 The Jelly reflects your attack!")
            print(f"You hit YOURSELF for {damage} damage!")
            if player is not None:
                player.take_hit(damage)
        else: #Dan gaat de damage dus normaal en dus op de jelly
            self.hp -= damage
            print(f"You successfully hit the Jelly for {damage} damage!")
            if self.hp > 0:
                print(self.monster_type, "has", self.hp, "hp left")
            else:
                print(self.monster_type, "is dissolved!")           
       
#De Evil_eyes(monster) zorgt ervoor dat de speler's armor kapot gaat. 
class Evil_eyes(Monster):
    def __init__(self, level):
        Monster.__init__(self, level)
        self.monster_type = "Evil_eyes"
        self.hp = self.max_hp = self.level * 13
        self.min_damage = self.level + 1
        self.max_damage = self.level * 3
        self.xp_value = 100 + self.level * 20
        self.gold_value = 7 + self.level * 50
        
    def verzwak_armor(self, player):
        if player.armor.defence <= 0:
            print("👁️ Your armor is already completely broken!")
            return

        if random.randint(1, 100) <= 45:
            print("👁️ The Evil Eyes stare into your soul...")
            print("🛡️ Your armor is CURSED!")
            print(" Your armor defence before:", player.armor.defence)

            player.armor.defence = max(0, player.armor.defence - 2)

            print("Your armor defence after Evil Eyes ATTACKKK:", player.armor.defence)
            print()
            
class Goo_skulls(Monster):
    def __init__(self, level):
        Monster.__init__(self, level)   
        self.monster_type = "Goo_skulls"
        self.hp = self.max_hp = self.level * 20
        self.min_damage = 1
        self.max_damage = self.level * 5
        self.xp_value = 100 + self.level * 20
        self.gold_value = 6 + self.level * 36
        self.crit_chance = max(30, level * 10)
        
    def attack(self):
        damage = random.randint(self.min_damage, self.max_damage)
        #crit hit?
        if random.randint(1, 100) <= self.crit_chance:
            print(self.monster_type, "makes a critical hit!")
            damage *= 2
            
        print(self.monster_type, "attacks for", damage, "damage")
        return damage



