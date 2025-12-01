import random
from Player import Player
from Item import Item, Weapon, Armor
from Monster import Monster, Skeleton, Troll
from Battle import Battle


player_name = input("What is your name?")
player = Player(player_name)

print()
print("Good luck", player_name, "Everyone is counting on you")
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








