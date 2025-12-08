import random
from Player import Player
from Item import Item, Weapon, Armor
from Monster import Monster, Skeleton, Troll
from Battle import Battle

player_name = " "
            while player_action not in ["A","B","C"]:
                player_name = input("Who do you want to be? (A): Ice king, (B): Finn, (C): Three trunks").upper()  #Speler kiest A, B of C 
                print()

player = Player(player_name) #Naam wordt A, B, C

if name == "A":
    player_type = "Ice king"
elif name == "B":
    player_type = "Finn"
elif name == "C":
    player_type = "Three trunks"
######################code bedenken die de types een type geeft
print()
print("Good luck", player_type, "Everyone is counting on you")
input("Press enter to enter the dungeon")


battle_count = 0

while player.hp > 0:
    print()
    print("-----")
    print()
    battle_count += 1
    print("Battle", battle_count)
    battle = Battle(player)
    battle.fight_battle() # start
    
print()
print("You have fought", battle_count, "battles")
print("Your final stats are:")
player.print_stats()
print()
print("Thanks for playing")









