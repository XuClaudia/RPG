from Player import Player
from Item import Item, Weapon, Armor
from Monster import Monster, Zombie, Candy, Vampire, Jelly, Evil_eyes, Goo_skulls
from Battle import Battle
from SaveGame import save_game, load_game, show_save_info
from Locations import LOCATIONS
import random
import time
import Ascii

def text_effect(text):
    for letter in text:
        print(letter, end="")
        time.sleep(0.02)

#---------------- SAVE GAME CHECK + GAMESTART -----------------------
player = None
has_save = show_save_info()


if has_save:
    choice = input("Load this save? (Y/N): ").upper()
    if choice == "Y":
        player = load_game()
        Ascii.display_art(player.name)
        print(f"Welcome back, {player.name}!")
    else:
        print("Starting a new game...\n")
        print("="*90)
Ascii.display_art("Start")
time.sleep(1.5)
starttekst = [
"            ~~  Adventure Time Come on, grab your friends  ~~",
"            ~~       We'll go to very distant lands        ~~",
"            ~~    With Jake the Dog and Finn the Human     ~~",
"            ~~ The fun will never end, it's Adventure Time ~~"
]
for tekst in starttekst:
    print(tekst)
    time.sleep(1.3)
            
input("                        [PRESS ENTER TO CONTINUE]")
print()
print()
print("-"*90)
print()


#---------------- KARAKTER KIEZEN -----------------------
if player is None:
    #spelertype
    player_name = " "
    while player_name not in ["A","B","C", "FINN", "ICE KING", "TREE TRUNKS"]:
        #Speler kiest A, B of C 
        player_name = input("Who do you want to be? (A): Ice king, (B): Finn, (C): Tree trunks").upper()  
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
 

    print("="*90)
    print("  Name: " + player.name)
    print("  Level: " + str(player.level) )
    print("  HP: " + str(player.hp) + "/" + str(player.max_hp))
    print("  XP: " + str(player.xp) + "/" + str(player.next_level_xp))
    print("  Gold: " + str(player.gold))
    print("-"*90 )
    input("[PRESS ENTER TO CONTINUE]")
    Ascii.display_art("Map")
    text_effect("Here is the game map!\nYou are now at the start of your journey...\n")
    text_effect("I think I spotted the Candy Kingdom in the distance, through the trees.\n")
    text_effect("Its gumdrop towers and candy cane spires are hard to miss,\n")
    text_effect("even from here.\n")
    text_effect("The forest path seems to lead right toward it.\n")
    text_effect("Let's move to there and see if there is need of any heroic assistance—\n")
    text_effect("or if we can at least find some sweet supplies.\n")
    
    for letter in "BE AWARE!!":
                print(letter, end=" ")
                time.sleep(0.25)
    input("\n[PRESS ENTER TO CONTINUE]")
    print()
    
#---------------- ROUTE ------------------------------------------------------
#---------------- BATTLE -----------------------------------------------------
#Ascii.display_art("Map")
current_location_index = 0
battle_count = 0
previous_level = player.level

while player.hp > 0 and current_location_index < len(LOCATIONS):
    location = LOCATIONS[current_location_index]
    # Checken of de speler de volgende level mag doen
    if player.level < location["unlock_level"]:
        print(f"\n🔒 {location['name']} is locked!")
        print(f"   Required level: {location['unlock_level']}")
        print(f"   Your level: {player.level}")
        print("\nYou need to gain more experience first!")
        time.sleep(1)
        battle_count += 1
        print(f"\n⚔️ BATTLE {battle_count} ⚔️")
        battle = Battle(player)
        battle.fight_battle()
    
    elif player.level >= location["unlock_level"]:
        print(f"\n🔒 {location['name']} is unlocked!")
        # Toon ASCII art
        Ascii.display_art("travel")
        time.sleep(2)
        if location["ascii"] in Ascii.ASCII:
            Ascii.display_art(location["ascii"])
        else:
            Ascii.display_art("Map")
                
        print("\n" + "="*90)
        print(f"📍 CURRENT LOCATION: {location['name']}")
        print("="*90)
        print(f"   {location['description']}")
        print(f"   Difficulty: {'★' * location['difficulty']}")
        print(f"   Shop: {'✓' if location['has_shop'] else '✗'}")
        print("-"*90)
        input("\n[PRESS ENTER TO CONTINUE]")
        
        text_effect(f"\n⚔️ You arrived {location['name']}!\n")
        if location["name"] == "Candy Kingdom":
            text_effect("The Candy Kingdom has fallen to darkness.\nIts once-sweet inhabitants are now twisted monsters\n")
            text_effect("🧟 Zombies with candy-stuck limbs, moaning for 'braaaains... and sprinkles!'\n")
            text_effect("🍭 Candy monsters with razor-sharp sugar crystal weapons\n")
            text_effect("🧛 Vampires drawn by the sweet, magical blood of candy creatures\n")
            text_effect("🌀 Jelly monsters wobbling through gumdrop fields\n")
            text_effect("👁 Evil Eyes peering from candy cane forests\n")
            text_effect("💀 Goo Skulls leaving slimy trails through powdered sugar\n")
            text_effect("hungry for any intruder who dares enter their sugary domain.\n")
        elif location["name"] == "Lumpy Space":
            text_effect("Something about Lumpy Space attracts the weirdest monsters in Ooo.\n Maybe it's the lumps,\n")
            text_effect("maybe it's the purple haze.\n")
            text_effect("💜 Zombies with lumpy, misshapen bodies\n")
            text_effect("💜 Candy monsters turned purple and irregular\n")
            text_effect("💜 Vampires distorted by the space's weirdness\n")
            text_effect("💜 And things that defy description...\n")
            text_effect("💜 Either way, you're surrounded.\n")
        elif location["name"] == "Fire Kingdom":
            text_effect("\nThe heat hits you like a physical force. Sweat evaporates instantly.\n")
            text_effect("🔥 Zombies whose rotting flesh crackles with embers\n")
            text_effect("🔥 Vampires with eyes like molten gold\n")
            text_effect("🔥 Candy creatures caramelized into deadly weapons\n")
            text_effect("🔥 Fire elementals born from the very volcanoes\n")
            text_effect("🔥 And other heat-born abominations...\n")
            time.sleep(3)    
            
        if location["name"] == "Surprise":
            #hier moeten random games komen en niet maar eentje
            print("\n🎮 MINIGAME TIME!")
            print("Guess the number between 1-10!")
            secret = random.randint(1, 10)
            guess = int(input("Your guess: "))
            if guess == secret:
                print("🎉 You win 50 gold!")
                player.gold += 50
            else:
                print(f"❌ Wrong! The number was {secret}")
                
        elif location["name"] == "End Boss":
            print("\nMUAHAHAHAHHAAA 👹 FINAL BOSS BATTLE!")
            time.sleep(2)
            battle_count += 1
            current_location_name = location["name"]  # ← Pak locatienaam
            battle = Battle(player, current_location_name)
            #battle = Battle(player)
            battle.fight_battle()
            
        else:
            time.sleep(1)  
            print("Get ready for battle!")
            input("[PRESS ENTER TO CONTINUE]")
            battle_count += 1
            current_location_name = location["name"]  # ← Pak locatienaam
            battle = Battle(player, current_location_name) 
            #battle = Battle(player)
            battle.fight_battle() #start
            
        if player.hp > 0 and current_location_index < len(LOCATIONS) - 1:
            Ascii.display_art("Map")
            if current_location_index == 0:
                loc1 = LOCATIONS[current_location_index + 1]
                loc2 = LOCATIONS[current_location_index + 3]
                go_next = ""
                while go_next not in ["A", "B"]:
                    go_next = input(f"\n➡️ Where do you want to go? (A){loc1['name']} (B){loc2['name']}").upper
                    #print(f"   Required level: {next_loc['unlock_level']}")
                if go_next == "A":
                    current_location_index += 1
                elif go_next == "B":
                    current_location_index += 3
            elif current_location_index == 1:
                current_location_index += 1
            elif current_location_index == 2:
                current_location_index = 4
                    
    
print()
print("You have fought", battle_count, "battles")
print("Your final stats are:")
player.print_stats()
print()
print("Thanks for playing")




