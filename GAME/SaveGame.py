import pickle
import os

SAVE_FILE = "savegame.dat"

def save_game(player):
    with open(SAVE_FILE, "wb") as file:
        pickle.dump(player, file)
    print("💾 Game saved!")

def load_game():
    if not os.path.exists(SAVE_FILE):
        print("❌ No save game found.")
        return None
    
    try:
        with open(SAVE_FILE, "rb") as file:
            player = pickle.load(file)
            print("✅ Save game loaded.")
            return player

    except Exception:
        print("❌ Save file corrupted or outdated.")
        return None

def show_save_info():
    if not os.path.exists(SAVE_FILE):
        return False
    
    with open(SAVE_FILE, "rb") as file:
        player = pickle.load(file)
        
        print("\n💾 Saved game found:")
        
    print("-" * 30)
    print("Name :", player.name)
    print("Level:", player.level)
    print("HP   :", f"{player.hp} / {player.max_hp}")
    print("Gold :", player.gold)
    print("-" * 30)
    return True

