import json
import os

# --- CORE FUNCTIONS ---

def load_vault():
    """Fetches missions from the local JSON database."""
    try:
        with open("vault_data.json", "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # Added JSONDecodeError handle in case the file gets corrupted
        return []

def save_vault(vault):
    """Safely writes current missions to the SSD."""
    try:
        with open("vault_data.json", "w") as file:
            json.dump(vault, file, indent=4)
        print("\n[SYSTEM] 💾 DATA SECURED TO VAULT_DATA.JSON")
    except Exception as e:
        print(f"\n[ERROR] Could not save data: {e}")

def add_goal(vault):
    """Captures new mission parameters from the Chief."""
    print("\n" + "-"*15 + " NEW MISSION ENTRY " + "-"*15)
    
    goal = input("CHIEF, WHAT IS THE GOAL?: ").strip()
    category = input("CATEGORY (Family/Health/Career): ").strip()

    if goal and category:
        entry = {"goal": goal, "category": category}
        vault.append(entry)
        print("✅ MISSION LOGGED SUCCESSFULLY")
    else:
        print("❌ FAILED: Mission or Category cannot be empty.")

def view_vault(vault):
    """Displays the mission status board."""
    print("\n" + "="*45)
    print(f"{'THE MISSION VAULT':^45}") # Centered Title
    print("="*45)

    if not vault:
        print(f"{'!!! VAULT EMPTY: NO MISSIONS DETECTED !!!':^45}")
    else:
        for item in vault:
            # Added dynamic spacing for a cleaner "Table" look
            cat_tag = f"[{item['category'].upper()}]"
            print(f"{cat_tag:<12} -> {item['goal']}")
            
    print("="*45)

# --- MAIN ENGINE ---

def main():
    dream_vault = load_vault()
    
    while True:
        print("\n[1] ADD MISSION | [2] VIEW VAULT | [3] EXIT")
        choice = input("COMMAND > ").strip()

        if choice == "1":
            add_goal(dream_vault)
            save_vault(dream_vault)
        elif choice == "2":
            view_vault(dream_vault)
        elif choice == "3":
            print("\nSECURE EXIT INITIALIZED... SEE YOU AT THE TOP, CHIEF. 🚀")
            break
        else:
            print("\n[!] INVALID COMMAND: PLEASE SELECT 1, 2, OR 3.")

if __name__ == "__main__":
    main()
