from Item import Weapon, Armor
from Player import Player
import Ascii
import time 

universal_items = [
    { "name": "Health_potion",
      "cost": 50,
      "type": "Healing",
      "description": "Restores 5 HP",
      "requirement": lambda player: player.gold >= 50, #lambda is een functie
      "effect": lambda player: player.heal(5)
      
    },
     {
        "name": "Grenade", 
        "cost": 110,
        "type": "Attack",
        "description": "Does +20 damage on next attack",
        "requirement": lambda player: player.gold >= 110,
        "effect": lambda player:(
            setattr(player, 'has_grenade', True),
            print("💣 You bought a grenade! Next attack will be explosive!")
        )
    }
    
]

character_specific_items = {
    "Finn": [
        {"name": "Sword_polish",
         "cost": 61,
         "type": "Weapon_upgrade",
         "description": "Sharpens your sword (+5 damage)",
         "requirement": lambda player: player.gold >= 61,
         "effect": lambda player: (
             setattr(player.weapon, 'min_damage', player.weapon.min_damage + 5),
             setattr(player.weapon, 'max_damage', player.weapon.max_damage + 5),
             print(f"✨ Sword polished! Damage: {player.weapon.min_damage} - {player.weapon.max_damage}"))

        },
        {"name": "Dragon🐉_sword",
         "cost": 157,
         "type": "Weapon",
         "description": "Legendary sword",
         "requirement": lambda player: player.gold >= 157,
         "effect": lambda player: player.equip_item( Weapon(player.level, player.name, "Dragon_sword")
        )}
    ],
    
    "Ice king": [
        {"name": "Ice Gem",
         "cost": 70,
         "type": "Weapon_upgrade",
         "description": "Makes ice spells 20% stronger",
         "requirement": lambda player: player.gold >= 70,
         "effect": lambda player: (
             setattr(player.weapon, 'min_damage', int(player.weapon.min_damage * 1.2)),
             setattr(player.weapon, 'max_damage', int(player.weapon.max_damage * 1.2)),
             print(f"❄ Ice magic boosted! Damage: {player.weapon.min_damage} - {player.weapon.max_damage}"))
        },
        {"name": "princess_love",
         "cost": 173,
         "type": "Healing",
         "description": "+20 HP",
         "requirement": lambda player: player.gold >= 173,
         "effect": lambda player: player.heal(20)
        }
    ],
    
    "Tree trunks": [
        {"name": "Fork",
         "cost": 76,
         "type": "Weapon",
         "description": "Do not underestimate",
         "requirement": lambda player: player.gold >= 76,
         "effect": lambda player: player.equip_item( Weapon(player.level, player.name, "Fork"))
        },
        
        {"name": "Apple Pie",
         "cost": 67,
         "type": "Healing",
         "description": "Restores 20 HP",
         "requirement": lambda player: player.gold >= 67,
         "effect": lambda player: (
              player.heal(20),
              print("🥧 Yum Yum! +20 HP!"))
        }
    ]
}

class Shop:
    def __init__(self, player):
        self.player = player
        self.available_items = []
        self.shop_setup()
        
    def shop_setup(self):
        #hier komen alle opties voor in de shop
        self.available_items = universal_items.copy() #elk karakter heeft sowieso de basis producten in de shop
        
        if self.player.name in character_specific_items: #per karakter verschillende shop
            self.available_items.extend(character_specific_items[self.player.name])
        
    
    def display_shop(self):
        #de interface voor de shop
        print("\n" + "$"*75)
        Ascii.display_art("Item shop")
        #print(self.player.name + "'s Item Shop")
        print("Your gold:" + str(self.player.gold))
        print("-"*75)
        
        for i, item in enumerate(self.available_items, 1): #enumerate geeft zowel element als index
            # Checken of speler dit item kan kopen
            can_buy = item["requirement"](self.player) #dit roept de functie op
            status = "✓" if can_buy else "✗" #verkorte weergave
            
            print(f"{i}. {item['name']} - {item['cost']} gold")
            print(f"   {item['description']}")
            print(f"   Type: {item['type']}")
            print(f"   Available: {status}")
            print()
        
    def buy_item(self, choice):
         if 1 <= choice <= len(self.available_items):
            item = self.available_items[choice-1]
            
            # Check requirements
            if item["requirement"](self.player): 
                if self.player.gold >= item["cost"]: #voldoen
                    self.player.gold -= item["cost"] # Betaal
                    item["effect"](self.player) # Voer effect uit
                    return True
                else:
                    print("\nNot enough gold!")
                    time.sleep(1)
            else:
                print("\nNot enough gold!")
                time.sleep(1)
         else:
             print("\n Invalid choice!")
         return False
        
    def shop_loop(self):
        while True:
            self.display_shop()
            choice = input("\nChoose an item (number) or leave [ENTER: 123]: ")
            
            if choice == "123":
                print("\nCome back anytime!")
                time.sleep(1)
                break
            elif choice.isdigit():
                item_number = int(choice)
                success = self.buy_item(item_number)
                if success:
                    time.sleep(1)
            else:
                print("Please enter a  number or '123' to leave")
              

