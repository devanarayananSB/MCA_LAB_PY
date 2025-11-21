import random
import time
inventory = []
lives = 3

def slow(text):
    """Typing effect"""
    for char in text:
        print(char, end="", flush=True)
        time.sleep(0.02)
    print()

def choice(options):
    """Input validation"""
    user = input(">> ").strip().lower()
    while user not in options:
        slow("Invalid choice. Try again.")
        user = input(">> ").strip().lower()
    return user

def puzzle():
    """Random logic puzzle"""
    global lives
    slow("\n🔐 A door slides down blocking your path.")
    slow(" A glowing message appears:\n")
    
    puzzles = [
        ("What number comes next? 2, 4, 8, 16, _", "32"),
        ("Solve: (12 ÷ 3) + (5 × 2) =", "14"),
        ("If 1=3, 2=3, 3=5, 4=4, 5=4 then 6=?", "3"),
        ("A clock shows 3:15. What angle between hour & minute hand?", "7.5")
    ]

    q, ans = random.choice(puzzles)
    slow(q)
    user = input("Answer: ").strip()

    if user == ans:
        slow("\n🔓 The door unlocks. You continue.")
    else:
        lives -= 1
        slow("\n❌ Wrong answer.")
        slow(f"❤️ Lives remaining: {lives}")

        if lives <= 0:
            slow("\n💀 You collapse in the maze... GAME OVER.")
            exit()

def treasure_room():
    slow("\n💼 You find a chest. Open it? (yes/no)")
    if choice(["yes", "no"]) == "yes":
        item = random.choice(["Silver Key", "Map Fragment", "Health Potion"])
        slow(f"\n✨ You found: {item}")
        inventory.append(item)
    else:
        slow("\nYou walk past it... hoping you won't regret it.")

def final_boss():
    global lives
    slow("\n🔥 You reach the final gate. A mechanical guardian awakens.\n")
    time.sleep(1)
    slow("It speaks: 'ONLY THE PREPARED MAY PASS.'")

    if "Silver Key" not in inventory:
        slow("\nYou don't have the Silver Key...")
        slow("The guardian attacks.")
        lives -= 1
        slow(f"❤️ Lives remaining: {lives}")
        if lives <= 0:
            slow("\n💀 GAME OVER.")
            exit()

    slow("\n🗝 You use the Silver Key. The guardian stands down.")
    slow("\nOne final question:")

    puzzle()
    slow("\n🎉 The gate opens... blinding white light surrounds you.")
    slow("You escape the labyrinth.")
    slow("\n🏆 **VICTORY.**\n")


slow("🧪 WELCOME TO THE CODE LABYRINTH.")
slow("You wake up inside a dark high-tech maze.\n")
time.sleep(1)

slow("Two paths appear before you:\n")
slow("1️⃣ Left — cold, silent, metallic halls.")
slow("2️⃣ Right — faint lights flickering ahead.")

path = choice(["1", "2"])

if path == "1":
    slow("\nYour footsteps echo. The air feels heavy.")
    puzzle()
    treasure_room()
else:
    slow("\nA buzzing noise grows louder... the maze feels alive.")
    treasure_room()
    puzzle()

slow("\nYou continue deeper...\n")
time.sleep(1)

final_boss()
