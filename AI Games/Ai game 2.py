import random
import json
import os
import time

# ============================================================
#                    SHADOWS OF THE VOID
#                 A Python Terminal RPG
# ============================================================

SAVE_FILE = "savegame.json"

# -----------------------------
# Colors / Terminal Formatting
# -----------------------------

RESET = "\033[0m"
BOLD = "\033[1m"

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
GRAY = "\033[90m"


def color(text, c):
    return f"{c}{text}{RESET}"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input(color("\nPress ENTER to continue...", GRAY))


def slow_print(text, delay=0.01):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def bar(current, maximum, length=20):
    if maximum <= 0:
        maximum = 1

    current = max(0, min(current, maximum))
    filled = int((current / maximum) * length)

    return (
        color("█" * filled, GREEN)
        + color("░" * (length - filled), GRAY)
    )


# ============================================================
#                         ITEMS
# ============================================================

WEAPONS = {
    "Rusty Sword": {
        "damage": 8,
        "crit": 0.05,
        "rarity": "Common"
    },

    "Iron Blade": {
        "damage": 13,
        "crit": 0.08,
        "rarity": "Common"
    },

    "Knight Sword": {
        "damage": 19,
        "crit": 0.12,
        "rarity": "Rare"
    },

    "Shadow Fang": {
        "damage": 27,
        "crit": 0.18,
        "rarity": "Epic"
    },

    "Void Reaper": {
        "damage": 38,
        "crit": 0.25,
        "rarity": "Legendary"
    }
}

ARMORS = {
    "Cloth Armor": {
        "defense": 1,
        "rarity": "Common"
    },

    "Leather Armor": {
        "defense": 4,
        "rarity": "Common"
    },

    "Iron Armor": {
        "defense": 8,
        "rarity": "Rare"
    },

    "Shadow Armor": {
        "defense": 13,
        "rarity": "Epic"
    },

    "Void Armor": {
        "defense": 20,
        "rarity": "Legendary"
    }
}


# ============================================================
#                         ENEMIES
# ============================================================

ENEMIES = {
    "Goblin": {
        "hp": 35,
        "damage": 7,
        "defense": 1,
        "xp": 15,
        "gold": 8
    },

    "Skeleton": {
        "hp": 45,
        "damage": 10,
        "defense": 2,
        "xp": 20,
        "gold": 12
    },

    "Dark Wolf": {
        "hp": 55,
        "damage": 13,
        "defense": 3,
        "xp": 28,
        "gold": 16
    },

    "Shadow Knight": {
        "hp": 80,
        "damage": 18,
        "defense": 7,
        "xp": 45,
        "gold": 30
    },

    "Void Beast": {
        "hp": 120,
        "damage": 25,
        "defense": 10,
        "xp": 75,
        "gold": 50
    }
}


BOSSES = {
    "The Forgotten King": {
        "hp": 300,
        "damage": 30,
        "defense": 12,
        "xp": 250,
        "gold": 300
    },

    "The Void Lord": {
        "hp": 500,
        "damage": 42,
        "defense": 18,
        "xp": 500,
        "gold": 750
    }
}


# ============================================================
#                         PLAYER
# ============================================================

class Player:

    def __init__(self):
        self.name = "Hero"

        self.level = 1
        self.xp = 0
        self.gold = 25

        self.max_hp = 100
        self.hp = 100

        self.base_damage = 5
        self.base_defense = 0

        self.weapon = "Rusty Sword"
        self.armor = "Cloth Armor"

        self.potions = 3

        self.location = "Village"

        self.kills = 0
        self.bosses_defeated = 0

        self.inventory = [
            "Rusty Sword",
            "Cloth Armor"
        ]

    # -------------------------
    # Stats
    # -------------------------

    def weapon_damage(self):
        return WEAPONS[self.weapon]["damage"]

    def defense(self):
        return (
            self.base_defense
            + ARMORS[self.armor]["defense"]
        )

    def total_damage(self):
        return self.base_damage + self.weapon_damage()

    def crit_chance(self):
        return WEAPONS[self.weapon]["crit"]

    def xp_needed(self):
        return 50 + (self.level - 1) * 35

    # -------------------------
    # Level Up
    # -------------------------

    def gain_xp(self, amount):
        self.xp += amount

        print(
            color(
                f"\n+{amount} XP",
                CYAN
            )
        )

        while self.xp >= self.xp_needed():

            self.xp -= self.xp_needed()
            self.level += 1

            self.max_hp += 20
            self.hp = self.max_hp

            self.base_damage += 3
            self.base_defense += 1

            print()
            print(color("★ LEVEL UP! ★", YELLOW))
            print(
                color(
                    f"You reached level {self.level}!",
                    GREEN
                )
            )

            print("+20 maximum HP")
            print("+3 base damage")
            print("+1 defense")
            print("Your HP has been restored!")

    # -------------------------
    # Inventory
    # -------------------------

    def add_item(self, item):
        if item not in self.inventory:
            self.inventory.append(item)

    # -------------------------
    # Potion
    # -------------------------

    def use_potion(self):

        if self.potions <= 0:
            print(color("You have no potions.", RED))
            return False

        if self.hp >= self.max_hp:
            print(color("Your HP is already full.", YELLOW))
            return False

        old_hp = self.hp

        self.hp = min(
            self.max_hp,
            self.hp + 40
        )

        self.potions -= 1

        print(
            color(
                f"You restored {self.hp - old_hp} HP!",
                GREEN
            )
        )

        return True

    # -------------------------
    # Status
    # -------------------------

    def status(self):

        clear()

        print(color("=" * 60, CYAN))
        print(color("                         HERO", BOLD))
        print(color("=" * 60, CYAN))

        print(f"\nName: {self.name}")
        print(f"Level: {self.level}")

        print(
            f"XP: {self.xp}/{self.xp_needed()}"
        )

        print(
            f"HP: {self.hp}/{self.max_hp} "
            f"[{bar(self.hp, self.max_hp)}]"
        )

        print(f"Damage: {self.total_damage()}")
        print(f"Defense: {self.defense()}")
        print(
            f"Critical Chance: "
            f"{int(self.crit_chance() * 100)}%"
        )

        print(f"\nWeapon: {self.weapon}")
        print(f"Armor: {self.armor}")

        print(f"\nGold: {self.gold}")
        print(f"Potions: {self.potions}")
        print(f"Enemies defeated: {self.kills}")
        print(f"Bosses defeated: {self.bosses_defeated}")

        pause()


# ============================================================
#                         ENEMY CLASS
# ============================================================

class Enemy:

    def __init__(self, name, boss=False):

        data = (
            BOSSES[name]
            if boss
            else ENEMIES[name]
        )

        self.name = name
        self.max_hp = data["hp"]
        self.hp = data["hp"]

        self.damage = data["damage"]
        self.defense = data["defense"]

        self.xp = data["xp"]
        self.gold = data["gold"]

        self.boss = boss


# ============================================================
#                       COMBAT SYSTEM
# ============================================================

def choose_enemy(area):

    if area == "Forest":
        names = [
            "Goblin",
            "Goblin",
            "Skeleton",
            "Dark Wolf"
        ]

    elif area == "Ruins":
        names = [
            "Skeleton",
            "Dark Wolf",
            "Shadow Knight"
        ]

    elif area == "Void":
        names = [
            "Shadow Knight",
            "Void Beast"
        ]

    else:
        names = ["Goblin"]

    return random.choice(names)


def combat(player, enemy):

    clear()

    print(color("=" * 60, RED))
    print(color(f"              BATTLE: {enemy.name}", BOLD))
    print(color("=" * 60, RED))

    if enemy.boss:
        print(color("\n!!! BOSS BATTLE !!!", MAGENTA))

    while enemy.hp > 0 and player.hp > 0:

        print("\n")
        print(
            f"{color(player.name, BLUE)} "
            f"HP: {player.hp}/{player.max_hp}"
        )

        print(
            f"{color(enemy.name, RED)} "
            f"HP: {enemy.hp}/{enemy.max_hp}"
        )

        print()
        print("1. Attack")
        print("2. Heavy Attack")
        print("3. Use Potion")
        print("4. Run")

        choice = input("\n> ").strip()

        # -------------------------
        # Attack
        # -------------------------

        if choice == "1":

            damage = player.total_damage()

            # Random variation
            damage += random.randint(-3, 4)

            # Critical hit
            if random.random() < player.crit_chance():

                damage *= 2

                print(
                    color(
                        "\nCRITICAL HIT!",
                        YELLOW
                    )
                )

            damage = max(
                1,
                damage - enemy.defense
            )

            enemy.hp -= damage

            print(
                color(
                    f"You dealt {damage} damage!",
                    GREEN
                )
            )

        # -------------------------
        # Heavy Attack
        # -------------------------

        elif choice == "2":

            if random.random() < 0.65:

                damage = int(
                    player.total_damage() * 1.8
                )

                damage = max(
                    1,
                    damage - enemy.defense
                )

                enemy.hp -= damage

                print(
                    color(
                        f"\nHeavy attack dealt {damage} damage!",
                        YELLOW
                    )
                )

            else:

                print(
                    color(
                        "\nYour heavy attack missed!",
                        RED
                    )
                )

        # -------------------------
        # Potion
        # -------------------------

        elif choice == "3":

            if not player.use_potion():
                continue

        # -------------------------
        # Run
        # -------------------------

        elif choice == "4":

            if enemy.boss:

                print(
                    color(
                        "\nYou cannot run from a boss!",
                        RED
                    )
                )

                continue

            if random.random() < 0.55:

                print(
                    color(
                        "\nYou escaped!",
                        YELLOW
                    )
                )

                time.sleep(1)
                return False

            else:

                print(
                    color(
                        "\nYou failed to escape!",
                        RED
                    )
                )

        else:

            print(
                color(
                    "\nInvalid choice.",
                    RED
                )
            )

            continue

        # -------------------------
        # Enemy Turn
        # -------------------------

        if enemy.hp > 0:

            # Enemy has chance to miss
            if random.random() < 0.10:

                print(
                    color(
                        f"{enemy.name} missed!",
                        CYAN
                    )
                )

            else:

                damage = enemy.damage

                # Player defense
                damage -= player.defense()

                damage = max(
                    1,
                    damage
                )

                # Boss special attack
                if (
                    enemy.boss
                    and random.random() < 0.20
                ):

                    damage *= 2

                    print(
                        color(
                            f"\n{enemy.name} used a "
                            f"DEVASTATING ATTACK!",
                            MAGENTA
                        )
                    )

                player.hp -= damage

                print(
                    color(
                        f"{enemy.name} dealt "
                        f"{damage} damage!",
                        RED
                    )
                )

        time.sleep(0.7)

    # -------------------------
    # Player Dead
    # -------------------------

    if player.hp <= 0:

        player.hp = 0

        print(
            color(
                "\nYou have been defeated...",
                RED
            )
        )

        pause()
        return "dead"

    # -------------------------
    # Enemy Dead
    # -------------------------

    print(
        color(
            f"\nYou defeated {enemy.name}!",
            GREEN
        )
    )

    player.kills += 1

    player.gold += enemy.gold
    player.gain_xp(enemy.xp)

    print(
        color(
            f"+{enemy.gold} gold",
            YELLOW
        )
    )

    # -------------------------
    # Loot
    # -------------------------

    if random.random() < 0.25:

        loot = random.choice(
            list(WEAPONS.keys())
            + list(ARMORS.keys())
        )

        player.add_item(loot)

        print(
            color(
                f"\n★ LOOT FOUND: {loot} ★",
                MAGENTA
            )
        )

    if random.random() < 0.15:

        player.potions += 1

        print(
            color(
                "\nYou found a healing potion!",
                GREEN
            )
        )

    pause()

    return True


# ============================================================
#                         SHOP
# ============================================================

def shop(player):

    while True:

        clear()

        print(color("=" * 60, YELLOW))
        print(color("                         SHOP", BOLD))
        print(color("=" * 60, YELLOW))

        print(f"\nGold: {player.gold}")

        print("\n1. Healing Potion - 15 gold")
        print("2. Iron Blade - 80 gold")
        print("3. Knight Sword - 180 gold")
        print("4. Iron Armor - 120 gold")
        print("5. Shadow Armor - 300 gold")
        print("6. Leave")

        choice = input("\n> ").strip()

        if choice == "1":

            if player.gold >= 15:

                player.gold -= 15
                player.potions += 1

                print(
                    color(
                        "Potion purchased!",
                        GREEN
                    )
                )

            else:
                print(color("Not enough gold.", RED))

            pause()

        elif choice == "2":

            buy_weapon(
                player,
                "Iron Blade",
                80
            )

        elif choice == "3":

            buy_weapon(
                player,
                "Knight Sword",
                180
            )

        elif choice == "4":

            buy_armor(
                player,
                "Iron Armor",
                120
            )

        elif choice == "5":

            buy_armor(
                player,
                "Shadow Armor",
                300
            )

        elif choice == "6":
            break

        else:
            print(color("Invalid choice.", RED))
            pause()


def buy_weapon(player, name, price):

    if name in player.inventory:

        print(
            color(
                "You already own this weapon.",
                YELLOW
            )
        )

    elif player.gold < price:

        print(
            color(
                "Not enough gold.",
                RED
            )
        )

    else:

        player.gold -= price
        player.add_item(name)

        print(
            color(
                f"You bought {name}!",
                GREEN
            )
        )

    pause()


def buy_armor(player, name, price):

    if name in player.inventory:

        print(
            color(
                "You already own this armor.",
                YELLOW
            )
        )

    elif player.gold < price:

        print(
            color(
                "Not enough gold.",
                RED
            )
        )

    else:

        player.gold -= price
        player.add_item(name)

        print(
            color(
                f"You bought {name}!",
                GREEN
            )
        )

    pause()


# ============================================================
#                         EQUIPMENT
# ============================================================

def equipment(player):

    while True:

        clear()

        print(color("=" * 60, BLUE))
        print(color("                      EQUIPMENT", BOLD))
        print(color("=" * 60, BLUE))

        print("\nWeapons:")

        weapon_items = [
            item for item in player.inventory
            if item in WEAPONS
        ]

        for i, item in enumerate(weapon_items, 1):

            equipped = (
                " [EQUIPPED]"
                if item == player.weapon
                else ""
            )

            print(
                f"{i}. {item} "
                f"({WEAPONS[item]['rarity']}) "
                f"- {WEAPONS[item]['damage']} damage"
                f"{equipped}"
            )

        print("\nArmor:")

        armor_items = [
            item for item in player.inventory
            if item in ARMORS
        ]

        for i, item in enumerate(armor_items, 1):

            equipped = (
                " [EQUIPPED]"
                if item == player.armor
                else ""
            )

            print(
                f"{i}. {item} "
                f"({ARMORS[item]['rarity']}) "
                f"- {ARMORS[item]['defense']} defense"
                f"{equipped}"
            )

        print("\nType:")
        print("W1, W2, W3... to equip a weapon")
        print("A1, A2, A3... to equip armor")
        print("X to leave")

        choice = input("\n> ").strip().upper()

        if choice == "X":
            break

        if choice.startswith("W"):

            try:

                number = int(choice[1:]) - 1

                if 0 <= number < len(weapon_items):

                    player.weapon = weapon_items[number]

                    print(
                        color(
                            f"Equipped {player.weapon}!",
                            GREEN
                        )
                    )

                else:
                    print(color("Invalid weapon.", RED))

            except ValueError:
                print(color("Invalid choice.", RED))

            pause()

        elif choice.startswith("A"):

            try:

                number = int(choice[1:]) - 1

                if 0 <= number < len(armor_items):

                    player.armor = armor_items[number]

                    print(
                        color(
                            f"Equipped {player.armor}!",
                            GREEN
                        )
                    )

                else:
                    print(color("Invalid armor.", RED))

            except ValueError:
                print(color("Invalid choice.", RED))

            pause()


# ============================================================
#                         EXPLORATION
# ============================================================

def explore(player):

    if player.location == "Village":

        print(
            color(
                "\nYou cannot fight enemies in the village.",
                YELLOW
            )
        )

        pause()
        return

    print(
        color(
            f"\nYou explore the {player.location}...",
            CYAN
        )
    )

    time.sleep(1)

    roll = random.random()

    # Enemy
    if roll < 0.70:

        enemy_name = choose_enemy(
            player.location
        )

        enemy = Enemy(enemy_name)

        result = combat(
            player,
            enemy
        )

        if result == "dead":
            return "dead"

    # Treasure
    elif roll < 0.90:

        gold = random.randint(15, 60)

        player.gold += gold

        print(
            color(
                f"\nYou found a treasure chest!",
                YELLOW
            )
        )

        print(
            color(
                f"+{gold} gold",
                YELLOW
            )
        )

        if random.random() < 0.30:

            player.potions += 1

            print(
                color(
                    "You also found a potion!",
                    GREEN
                )
            )

        pause()

    # Nothing
    else:

        print(
            color(
                "\nYou found nothing...",
                GRAY
            )
        )

        pause()


# ============================================================
#                         BOSS
# ============================================================

def boss_battle(player):

    clear()

    if player.location == "Forest":

        boss_name = "The Forgotten King"

    elif player.location == "Void":

        boss_name = "The Void Lord"

    else:

        print(
            color(
                "There is no boss here.",
                RED
            )
        )

        pause()
        return

    enemy = Enemy(
        boss_name,
        boss=True
    )

    result = combat(
        player,
        enemy
    )

    if result is True:

        player.bosses_defeated += 1

        print(
            color(
                "\n★ BOSS DEFEATED ★",
                MAGENTA
            )
        )

        if boss_name == "The Forgotten King":

            print(
                color(
                    "A dark portal has appeared...",
                    MAGENTA
                )
            )

        elif boss_name == "The Void Lord":

            print()
            print(color("=" * 60, YELLOW))
            print(color("             YOU SAVED THE WORLD!", YELLOW))
            print(color("=" * 60, YELLOW))
            print()
            print(
                "The Void Lord has been destroyed."
            )
            print(
                "The darkness covering the land disappears."
            )
            print(
                "You have completed your journey."
            )

            pause()


# ============================================================
#                         TRAVEL
# ============================================================

def travel(player):

    clear()

    print(color("=" * 60, CYAN))
    print(color("                       TRAVEL", BOLD))
    print(color("=" * 60, CYAN))

    print("\nCurrent location:", player.location)

    print("\n1. Village")
    print("2. Forest")
    print("3. Ruins")

    if player.bosses_defeated >= 1:
        print("4. Void")

    print("5. Cancel")

    choice = input("\n> ").strip()

    if choice == "1":
        player.location = "Village"

    elif choice == "2":
        player.location = "Forest"

    elif choice == "3":

        if player.level >= 3:
            player.location = "Ruins"

        else:

            print(
                color(
                    "\nYou need to be level 3.",
                    RED
                )
            )

            pause()
            return

    elif choice == "4":

        if player.bosses_defeated >= 1:
            player.location = "Void"

        else:

            print(
                color(
                    "\nThe Void is locked.",
                    RED
                )
            )

            pause()
            return

    elif choice == "5":
        return

    else:

        print(
            color(
                "\nInvalid choice.",
                RED
            )
        )

        pause()
        return

    print(
        color(
            f"\nYou traveled to {player.location}.",
            GREEN
        )
    )

    pause()


# ============================================================
#                         SAVE SYSTEM
# ============================================================

def save_game(player):

    data = {
        "name": player.name,
        "level": player.level,
        "xp": player.xp,
        "gold": player.gold,
        "max_hp": player.max_hp,
        "hp": player.hp,
        "base_damage": player.base_damage,
        "base_defense": player.base_defense,
        "weapon": player.weapon,
        "armor": player.armor,
        "potions": player.potions,
        "location": player.location,
        "kills": player.kills,
        "bosses_defeated": player.bosses_defeated,
        "inventory": player.inventory
    }

    try:

        with open(
            SAVE_FILE,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                data,
                file,
                indent=4
            )

        print(
            color(
                "\nGame saved!",
                GREEN
            )
        )

    except Exception as error:

        print(
            color(
                f"\nCould not save game: {error}",
                RED
            )
        )

    pause()


def load_game():

    if not os.path.exists(SAVE_FILE):
        return None

    try:

        with open(
            SAVE_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        player = Player()

        player.name = data["name"]
        player.level = data["level"]
        player.xp = data["xp"]
        player.gold = data["gold"]

        player.max_hp = data["max_hp"]
        player.hp = data["hp"]

        player.base_damage = data["base_damage"]
        player.base_defense = data["base_defense"]

        player.weapon = data["weapon"]
        player.armor = data["armor"]

        player.potions = data["potions"]
        player.location = data["location"]

        player.kills = data["kills"]
        player.bosses_defeated = data["bosses_defeated"]

        player.inventory = data["inventory"]

        return player

    except Exception:
        return None


# ============================================================
#                         INTRO
# ============================================================

def intro():

    clear()

    print(color("=" * 60, MAGENTA))
    print(
        color(
            "                 SHADOWS OF THE VOID",
            BOLD
        )
    )
    print(color("=" * 60, MAGENTA))

    print()
    slow_print(
        "The world was once protected by an ancient kingdom."
    )

    slow_print(
        "Then the Void opened."
    )

    slow_print(
        "Monsters flooded across the land."
    )

    slow_print(
        "The kingdom fell."
    )

    slow_print(
        "Now only one hero remains."
    )

    print()

    name = input(
        color(
            "Enter your hero's name: ",
            CYAN
        )
    ).strip()

    if not name:
        name = "Hero"

    return name


# ============================================================
#                         MAIN MENU
# ============================================================

def main_menu(player):

    while True:

        clear()

        print(color("=" * 60, CYAN))
        print(
            color(
                "                  SHADOWS OF THE VOID",
                BOLD
            )
        )
        print(color("=" * 60, CYAN))

        print(
            f"\n{color(player.name, BLUE)} "
            f"Lv.{player.level}"
        )

        print(
            f"Location: {player.location}"
        )

        print()

        print("1. Explore")
        print("2. Travel")
        print("3. Equipment")
        print("4. Shop")
        print("5. Character")
        print("6. Save Game")
        print("7. Boss")
        print("8. Quit")

        choice = input("\n> ").strip()

        if choice == "1":

            result = explore(player)

            if result == "dead":
                return "dead"

        elif choice == "2":

            travel(player)

        elif choice == "3":

            equipment(player)

        elif choice == "4":

            if player.location == "Village":
                shop(player)

            else:

                print(
                    color(
                        "\nThe shop is only available in the village.",
                        RED
                    )
                )

                pause()

        elif choice == "5":

            player.status()

        elif choice == "6":

            save_game(player)

        elif choice == "7":

            if player.location in ["Forest", "Void"]:

                boss_battle(player)

            else:

                print(
                    color(
                        "\nThere is no boss here.",
                        RED
                    )
                )

                pause()

        elif choice == "8":

            clear()

            print(
                color(
                    "Thanks for playing!",
                    CYAN
                )
            )

            return "quit"

        else:

            print(
                color(
                    "Invalid choice.",
                    RED
                )
            )

            pause()


# ============================================================
#                         GAME START
# ============================================================

def main():

    clear()

    print(color("SHADOWS OF THE VOID", MAGENTA))
    print()

    print("1. New Game")
    print("2. Load Game")
    print("3. Quit")

    choice = input("\n> ").strip()

    if choice == "1":

        player = Player()
        player.name = intro()

    elif choice == "2":

        player = load_game()

        if player is None:

            print(
                color(
                    "\nNo valid save file found.",
                    RED
                )
            )

            pause()

            player = Player()
            player.name = intro()

        else:

            print(
                color(
                    f"\nWelcome back, {player.name}!",
                    GREEN
                )
            )

            pause()

    else:

        return

    while True:

        result = main_menu(player)

        if result == "dead":

            clear()

            print(color("=" * 60, RED))
            print(color("                       YOU DIED", BOLD))
            print(color("=" * 60, RED))

            print()
            print(f"Level reached: {player.level}")
            print(f"Enemies defeated: {player.kills}")
            print(f"Bosses defeated: {player.bosses_defeated}")

            print("\n1. New Game")
            print("2. Load Save")
            print("3. Quit")

            choice = input("\n> ").strip()

            if choice == "1":

                player = Player()
                player.name = intro()

            elif choice == "2":

                loaded = load_game()

                if loaded:

                    player = loaded

                else:

                    print(
                        color(
                            "No save found.",
                            RED
                        )
                    )

                    pause()

            else:

                break

        else:
            break


if __name__ == "__main__":
    main()
