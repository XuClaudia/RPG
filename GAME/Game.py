import random
import time
from Player import Player
from Item import Item, Weapon, Armor
from Monster import Monster, Zombie, Candy, Vampire, Jelly, Evil_eyes, Goo_skulls
from Battle import Battle
import Ascii
def text_effect(text):
    for letter in text:
        print(letter, end="")
        time.sleep(0.05)

#startscherm
starttekst = [
    "Hey! Hello there!",
    "",
    "~~  Adventure Time Come on, grab your friends",
    "~~  We'll go to very distant lands",
    "~~  With Jake the Dog and Finn the Human",
    "~~  The fun will never end, it's Adventure Time"
    ]

for tekst in starttekst:
    print(tekst)
    time.sleep(1.3)
    

input("[PRESS ENTER TO CONTINUE]")
print("-"*75)

#spelertype 
player_name = " "
while player_name not in ["A","B","C", "FINN", "ICE KING", "TREE TRUNKS"]:
    player_name = input("Who do you want to be? (A): Ice king, (B): Finn, (C): Tree trunks\n").upper()  #Speler kiest A, B of C 
    print()

#player = Player(player_name)
if player_name == "A" or player_name == "Ice king":
    player = Player("Ice king")
    Ascii.display_art("Ice king")
elif player_name == "B" or player_name == "Finn":
    player = Player("Finn")
    Ascii.display_art("Finn")
elif player_name == "C" or player_name == "Tree trunks":
    player = Player("Tree trunks")
    Ascii.display_art("Tree trunks")
 

    
text_effect("Hi " + player.name + ", you are entering a world full of adventure....\n")
#HIER MOET NOG TEKST BIJ VERZONNEN WORDEN
for letter in "BE AWARE!!":
            print(letter, end=" ")
            time.sleep(0.25)
            
print()         
input("[PRESS ENTER TO CONTINUE]")
print("-"*75)

#HIER MOET SOWIESO NOG IETS OF EEN VERHAALTJE MAAR DA IS KWA CODE NI HEEL INTERESSANT
#OF WE DOEN IETS VAN EEN MAP TOEVOEGEN?? DIE HIER NU KOMT
#GW IETS ZODAT JE NIET BEGINT MET WOW GEVECHT
#VISUEEL TEXT MAP???

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

























