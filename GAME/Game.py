#tekst letter voor letter laten verschijnen en niet in een pak
import random
import time
from Player import Player
from Item import Item, Weapon, Armor
from Monster import Monster, Zombie, Candy, Vampire, Jelly, Evil_eyes, Goo_skulls
from Battle import Battle
def text_effect(text):
    for letter in text:
        print(letter, end="")
        time.sleep(0.05)
#welcome screen
print("Hey! Hello there!")
input("[PRESS ENTER TO CONTINUE]")
print()
print("~~  Adventure Time Come on, grab your friends")
time.sleep(1)
print("~~  We'll go to very distant lands")
time.sleep(1.5)
print("~~  With Jake the Dog and Finn the Human")
time.sleep(2)
print("~~  The fun will never end, it's Adventure Time")
time.sleep(1.5)
print()
input("[PRESS ENTER TO CONTINUE]")
print()

#spelertype 
player_name = " "
while player_name not in ["A","B","C", "FINN", "ICE KING", "THREE TRUNKS"]:
    player_name = input("Who do you want to be? (A): Ice king, (B): Finn, (C): Three trunks\n").upper()  #Speler kiest A, B of C 
    print()


if player_name == "A" or player_name == "Ice king":
    player = Player("Ice king") 
elif player_name == "B" or player_name == "Finn":
    player = Player("Finn") 
elif player_name == "C" or player_name == "Three trunks":
    player = Player("Three trunks") 
 
#player = Player(player_name)
    
print()
text_effect("Hi " + player.name + ", you are entering a world full of adventure....\n")
for letter in "BE AWARE!!":
            print(letter, end=" ")
            time.sleep(0.25)
            
print()         
input("[PRESS ENTER TO CONTINUE]")


battle_count = 0

while player.hp > 0:
    print()
    print("-----")
    print()
    battle_count += 1
    print("{BATTLE", battle_count, "}")
    battle = Battle(player)
    battle.fight_battle() #start
    
print()
print("You have fought", battle_count, "battles")
print("Your final stats are:")
player.print_stats()
print()
print("Thanks for playing")























