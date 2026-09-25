import os
import random
import time

# ============================================================
#                     RIDDLE MASTER
#              THE HOUSE OF A THOUSAND RIDDLES
# ============================================================

RESET = "\033[0m"

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


# ============================================================
#                         PLAYER
# ============================================================

class Player:

    def __init__(self):
        self.name = ""
        self.lives = 3
        self.coins = 0
        self.score = 0
        self.streak = 0
        self.best_streak = 0
        self.hints = 3
        self.room = 1
        self.riddles_solved = 0

    def correct(self, points):

        self.streak += 1

        self.best_streak = max(
            self.best_streak,
            self.streak
        )

        bonus = self.streak * 10

        self.score += points + bonus
        self.coins += 5

        self.riddles_solved += 1

        print()
        print(color("✓ CORRECT!", GREEN))
        print(
            color(
                f"+{points} points",
                YELLOW
            )
        )

        print(
            color(
                f"+{bonus} streak bonus",
                MAGENTA
            )
        )

        print(
            color(
                "+5 coins",
                YELLOW
            )
        )

    def wrong(self):

        self.lives -= 1
        self.streak = 0

        print()
        print(color("✗ WRONG!", RED))

        print(
            color(
                f"Lives remaining: {self.lives}",
                YELLOW
            )
        )


# ============================================================
#                         RIDDLES
# ============================================================

RIDDLES = [

    # --------------------------------------------------------
    # EASY
    # --------------------------------------------------------

    {
        "difficulty": "EASY",
        "points": 100,
        "riddle":
            "I have hands but cannot clap.\n"
            "I have a face but cannot smile.\n"
            "What am I?",
        "answers": ["clock", "a clock"],
        "hint":
            "You might look at me to know what time it is."
    },

    {
        "difficulty": "EASY",
        "points": 100,
        "riddle":
            "I get wetter the more I dry.\n"
            "What am I?",
        "answers": ["towel", "a towel"],
        "hint":
            "You probably use me after taking a shower."
    },

    {
        "difficulty": "EASY",
        "points": 100,
        "riddle":
            "I have many keys but cannot open a single door.\n"
            "What am I?",
        "answers": ["keyboard", "a keyboard"],
        "hint":
            "You are probably using one right now."
    },

    {
        "difficulty": "EASY",
        "points": 100,
        "riddle":
            "The more you take, the more you leave behind.\n"
            "What am I?",
        "answers": ["footsteps", "steps", "footprints"],
        "hint":
            "Think about walking."
    },

    # --------------------------------------------------------
    # MEDIUM
    # --------------------------------------------------------

    {
        "difficulty": "MEDIUM",
        "points": 200,
        "riddle":
            "I speak without a mouth\n"
            "and hear without ears.\n"
            "I have no body,\n"
            "but I come alive with wind.\n"
            "What am I?",
        "answers": ["echo", "an echo"],
        "hint":
            "You might hear me in a cave."
    },

    {
        "difficulty": "MEDIUM",
        "points": 200,
        "riddle":
            "I am always in front of you,\n"
            "but can never be seen.\n"
            "What am I?",
        "answers": ["future", "the future"],
        "hint":
            "It hasn't happened yet."
    },

    {
        "difficulty": "MEDIUM",
        "points": 200,
        "riddle":
            "What has cities, but no houses;\n"
            "forests, but no trees;\n"
            "and rivers, but no water?",
        "answers": ["map", "a map"],
        "hint":
            "You might use me when traveling."
    },

    {
        "difficulty": "MEDIUM",
        "points": 200,
        "riddle":
            "I have one eye but cannot see.\n"
            "What am I?",
        "answers": ["needle", "a needle"],
        "hint":
            "Something used for sewing."
    },

    # --------------------------------------------------------
    # HARD
    # --------------------------------------------------------

    {
        "difficulty": "HARD",
        "points": 350,
        "riddle":
            "The more of me there is,\n"
            "the less you can see.\n"
            "What am I?",
        "answers": ["darkness", "dark"],
        "hint":
            "Turn off the lights."
    },

    {
        "difficulty": "HARD",
        "points": 350,
        "riddle":
            "I can be cracked,\n"
            "made, told, and played.\n"
            "What am I?",
        "answers": ["joke", "a joke"],
        "hint":
            "People laugh when I am good."
    },

    {
        "difficulty": "HARD",
        "points": 350,
        "riddle":
            "I belong to you,\n"
            "but other people use me more than you do.\n"
            "What am I?",
        "answers": ["name", "your name", "my name"],
        "hint":
            "Other people call you by it."
    },

    {
        "difficulty": "HARD",
        "points": 350,
        "riddle":
            "What disappears as soon as you say its name?",
        "answers": ["silence", "quiet"],
        "hint":
            "You destroy it by making a sound."
    },

    # --------------------------------------------------------
    # VERY HARD
    # --------------------------------------------------------

    {
        "difficulty": "VERY HARD",
        "points": 500,
        "riddle":
            "I am not alive,\n"
            "but I grow.\n"
            "I don't have lungs,\n"
            "but I need air.\n"
            "I don't have a mouth,\n"
            "but water kills me.\n"
            "What am I?",
        "answers": ["fire", "a fire"],
        "hint":
            "Be careful around me."
    },

    {
        "difficulty": "VERY HARD",
        "points": 500,
        "riddle":
            "You see me once in June,\n"
            "twice in November,\n"
            "but not at all in May.\n"
            "What am I?",
        "answers": ["letter e", "e"],
        "hint":
            "Look at the spelling of the months."
    },

    {
        "difficulty": "VERY HARD",
        "points": 500,
        "riddle":
            "A man shaves several times a day,\n"
            "yet still has a beard.\n"
            "Who is he?",
        "answers": ["barber", "a barber"],
        "hint":
            "He shaves other people."
    },

    {
        "difficulty": "VERY HARD",
        "points": 500,
        "riddle":
            "I have no beginning,\n"
            "no end,\n"
            "and no middle.\n"
            "What am I?",
        "answers": ["circle", "a circle"],
        "hint":
            "Think of a perfectly round shape."
    }
]


# ============================================================
#                     SPECIAL RIDDLES
# ============================================================

BOSS_RIDDLES = [

    {
        "riddle":
            "I am taken from a mine,\n"
            "and shut inside a wooden case,\n"
            "from which I am never released,\n"
            "and yet almost everyone uses me.\n"
            "What am I?",
        "answers": [
            "pencil lead",
            "graphite",
            "lead"
        ],
        "hint":
            "You use me to write."
    },

    {
        "riddle":
            "A room has four corners.\n"
            "In each corner sits a cat.\n"
            "Each cat sees three cats.\n"
            "How many cats are in the room?",
        "answers": [
            "4",
            "four"
        ],
        "hint":
            "All four cats can see the other three."
    },

    {
        "riddle":
            "What can run but never walks,\n"
            "has a mouth but never talks,\n"
            "has a head but never weeps,\n"
            "and has a bed but never sleeps?",
        "answers": [
            "river",
            "a river"
        ],
        "hint":
            "It flows toward the sea."
    }
]


# ============================================================
#                      TITLE SCREEN
# ============================================================

def title_screen():

    clear()

    print(
        color(
            r"""
██████╗ ██╗██████╗ ██████╗ ██╗     ███████╗
██╔══██╗██║██╔══██╗██╔══██╗██║     ██╔════╝
██████╔╝██║██║  ██║██║  ██║██║     █████╗
██╔══██╗██║██║  ██║██║  ██║██║     ██╔══╝
██║  ██║██║██████╔╝██████╔╝███████╗███████╗
╚═╝  ╚═╝╚═╝╚═════╝ ╚═════╝ ╚══════╝╚══════╝

███╗   ███╗ █████╗ ███████╗████████╗███████╗██████╗
████╗ ████║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██╔████╔██║███████║███████╗   ██║   █████╗  ██████╔╝
██║╚██╔╝██║██╔══██║╚════██║   ██║   ██╔══╝  ██╔══██╗
██║ ╚═╝ ██║██║  ██║███████║   ██║   ███████╗██║  ██║
╚═╝     ╚═╝╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═╝  ╚═╝
            """,
            MAGENTA
        )
    )

    print(
        color(
            "\n              THE HOUSE OF RIDDLES",
            YELLOW
        )
    )

    print()
    print(
        "Solve the riddles.")
    print(
        "Unlock the doors.")
    print(
        "Reach the final chamber.")
    print(
        "Defeat the Riddle Master."
    )

    print()

    input(
        color(
            "Press ENTER to enter the house...",
            CYAN
        )
    )


# ============================================================
#                     STATUS BAR
# ============================================================

def status(player):

    print(
        color(
            "─" * 65,
            GRAY
        )
    )

    print(
        f"❤️ Lives: {player.lives}   "
        f"⭐ Score: {player.score}   "
        f"🪙 Coins: {player.coins}   "
        f"🔥 Streak: {player.streak}   "
        f"💡 Hints: {player.hints}"
    )

    print(
        color(
            "─" * 65,
            GRAY
        )
    )


# ============================================================
#                       INTRO
# ============================================================

def introduction(player):

    clear()

    print(
        color(
            "THE DOOR OPENS...",
            CYAN
        )
    )

    print()

    time.sleep(1)

    print(
        "A cold wind rushes past you."
    )

    print(
        "Inside the house, hundreds of locked doors"
    )

    print(
        "stretch into the darkness."
    )

    print()

    print(
        color(
            '"Only those who can answer may pass."',
            YELLOW
        )
    )

    print()

    print(
        "A strange voice whispers:"
    )

    print()

    print(
        color(
            '"Solve my riddles..."',
            MAGENTA
        )
    )

    print(
        color(
            '"...or remain here forever."',
            RED
        )
    )

    pause()


# ============================================================
#                       RIDDLE ROOM
# ============================================================

def ask_riddle(player, riddle):

    clear()

    print(
        color(
            f"╔════════════ ROOM {player.room} ════════════╗",
            CYAN
        )
    )

    print()

    print(
        color(
            f"Difficulty: {riddle['difficulty']}",
            YELLOW
        )
    )

    print(
        f"Reward: {riddle['points']} points"
    )

    print()

    status(player)

    print()

    print(
        color(
            riddle["riddle"],
            WHITE
        )
    )

    print()

    print(
        color(
            "Commands: ANSWER | hint | skip",
            GRAY
        )
    )

    print()

    while True:

        answer = input(
            "> "
        ).strip().lower()

        if answer == "hint":

            if player.hints <= 0:

                print(
                    color(
                        "You have no hints left.",
                        RED
                    )
                )

                continue

            player.hints -= 1

            print()

            print(
                color(
                    "HINT: " + riddle["hint"],
                    YELLOW
                )
            )

            continue

        if answer == "skip":

            print()

            print(
                color(
                    "You leave the room...",
                    GRAY
                )
            )

            player.streak = 0

            pause()

            return False

        if not answer:

            continue

        break

    # Flexible answer checking
    for accepted in riddle["answers"]:

        if answer == accepted:
            player.correct(
                riddle["points"]
            )

            pause()

            return True

    # Partial matching
    for accepted in riddle["answers"]:

        if (
            len(accepted) >= 4
            and accepted in answer
        ):

            player.correct(
                riddle["points"]
            )

            pause()

            return True

    player.wrong()

    print()

    print(
        color(
            "The correct answer was:",
            GRAY
        )
    )

    print(
        color(
            riddle["answers"][0],
            GREEN
        )
    )

    pause()

    return False


# ============================================================
#                       SHOP
# ============================================================

def shop(player):

    clear()

    print(
        color(
            "╔════════════ THE RIDDLE SHOP ════════════╗",
            YELLOW
        )
    )

    print()

    print(
        f"You have {player.coins} coins."
    )

    print()

    print(
        "1. Extra Life     - 20 coins"
    )

    print(
        "2. Hint           - 10 coins"
    )

    print(
        "3. 100 Points     - 25 coins"
    )

    print(
        "4. Leave"
    )

    print()

    choice = input(
        "> "
    ).strip()

    if choice == "1":

        if player.coins >= 20:

            player.coins -= 20
            player.lives += 1

            print(
                color(
                    "You bought an extra life!",
                    GREEN
                )
            )

        else:

            print(
                color(
                    "Not enough coins.",
                    RED
                )
            )

    elif choice == "2":

        if player.coins >= 10:

            player.coins -= 10
            player.hints += 1

            print(
                color(
                    "You bought a hint!",
                    GREEN
                )
            )

        else:

            print(
                color(
                    "Not enough coins.",
                    RED
                )
            )

    elif choice == "3":

        if player.coins >= 25:

            player.coins -= 25
            player.score += 100

            print(
                color(
                    "You gained 100 points!",
                    GREEN
                )
            )

        else:

            print(
                color(
                    "Not enough coins.",
                    RED
                )
            )

    pause()


# ============================================================
#                    RANDOM EVENT
# ============================================================

def random_event(player):

    events = [
        "coin",
        "hint",
        "nothing",
        "life"
    ]

    event = random.choice(events)

    if event == "coin":

        amount = random.randint(5, 15)

        player.coins += amount

        print(
            color(
                f"\nYou found {amount} coins!",
                YELLOW
            )
        )

    elif event == "hint":

        player.hints += 1

        print(
            color(
                "\nYou found a mysterious hint!",
                CYAN
            )
        )

    elif event == "life":

        if random.random() < 0.35:

            player.lives += 1

            print(
                color(
                    "\nA magical heart restores one life!",
                    GREEN
                )
            )

    else:

        print(
            color(
                "\nThe hallway is strangely quiet...",
                GRAY
            )
        )

    time.sleep(1)


# ============================================================
#                    BOSS CHAMBER
# ============================================================

def boss_chamber(player):

    clear()

    print(
        color(
            r"""
██████╗ ██╗██████╗ ██████╗ ██╗     ███████╗
██╔══██╗██║██╔══██╗██╔══██╗██║     ██╔════╝
██████╔╝██║██║  ██║██║  ██║██║     █████╗
██╔══██╗██║██║  ██║██║  ██║██║     ██╔══╝
██║  ██║██║██████╔╝██████╔╝███████╗███████╗
╚═╝  ╚═╝╚═╝╚═════╝ ╚═════╝ ╚══════╝╚══════╝
            """,
            RED
        )
    )

    print()

    print(
        color(
            "THE RIDDLE MASTER AWAKENS.",
            MAGENTA
        )
    )

    print()

    print(
        "You must solve TWO of THREE riddles"
    )

    print(
        "to unlock the final door."
    )

    pause()

    riddles = random.sample(
        BOSS_RIDDLES,
        3
    )

    solved = 0

    for number, riddle in enumerate(
        riddles,
        1
    ):

        clear()

        print(
            color(
                f"FINAL CHALLENGE {number}/3",
                RED
            )
        )

        print()

        print(
            riddle["riddle"]
        )

        print()

        print(
            color(
                "Type 'hint' for a clue.",
                GRAY
            )
        )

        print()

        answer = input(
            "> "
        ).strip().lower()

        if answer == "hint":

            print()

            print(
                color(
                    "HINT: " + riddle["hint"],
                    YELLOW
                )
            )

            answer = input(
                "\nYour answer: "
            ).strip().lower()

        if answer in riddle["answers"]:

            solved += 1

            player.score += 500

            print()

            print(
                color(
                    "✓ THE MASTER ACCEPTS YOUR ANSWER.",
                    GREEN
                )
            )

        else:

            player.lives -= 1

            print()

            print(
                color(
                    "✗ INCORRECT.",
                    RED
                )
            )

            print(
                "Answer:",
                riddle["answers"][0]
            )

        time.sleep(1)

    return solved >= 2


# ============================================================
#                       VICTORY
# ============================================================

def victory(player):

    clear()

    print(
        color(
            r"""
██╗   ██╗██╗ ██████╗████████╗ ██████╗ ██████╗ ██╗   ██╗
╚██╗ ██╔╝██║██╔════╝╚══██╔══╝██╔═══██╗██╔══██╗╚██╗ ██╔╝
 ╚████╔╝ ██║██║        ██║   ██║   ██║██████╔╝ ╚████╔╝
  ╚██╔╝  ██║██║        ██║   ██║   ██║██╔══██╗  ╚██╔╝
   ██║   ██║╚██████╗   ██║   ╚██████╔╝██║  ██║   ██║
   ╚═╝   ╚═╝ ╚═════╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝   ╚═╝
            """,
            GREEN
        )
    )

    print()

    print(
        color(
            "THE FINAL DOOR OPENS!",
            YELLOW
        )
    )

    print()

    print(
        "You have escaped the House of Riddles."
    )

    print()

    print(
        f"⭐ Final Score: {player.score}"
    )

    print(
        f"🔥 Best Streak: {player.best_streak}"
    )

    print(
        f"🧩 Riddles Solved: {player.riddles_solved}"
    )

    print(
        f"🪙 Coins: {player.coins}"
    )

    print()

    print(
        color(
            "THE RIDDLE MASTER HAS BEEN DEFEATED.",
            MAGENTA
        )
    )

    pause()


# ============================================================
#                       GAME OVER
# ============================================================

def game_over(player):

    clear()

    print(
        color(
            """
 ██████╗  █████╗ ███╗   ███╗███████╗
██╔════╝ ██╔══██╗████╗ ████║██╔════╝
██║  ███╗███████║██╔████╔██║█████╗
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝
            """,
            RED
        )
    )

    print()

    print(
        "The house has claimed another victim."
    )

    print()

    print(
        f"Score: {player.score}"
    )

    print(
        f"Riddles solved: {player.riddles_solved}"
    )

    print(
        f"Best streak: {player.best_streak}"
    )

    pause()


# ============================================================
#                         MAIN GAME
# ============================================================

def main():

    title_screen()

    player = Player()

    introduction(player)

    # Shuffle normal riddles
    riddles = RIDDLES.copy()

    random.shuffle(riddles)

    # --------------------------------------------------------
    # Main rooms
    # --------------------------------------------------------

    for riddle in riddles:

        player.room += 1

        result = ask_riddle(
            player,
            riddle
        )

        if player.lives <= 0:

            game_over(player)
            return

        # Random hallway event
        if random.random() < 0.25:

            random_event(player)

        # Shop every few rooms
        if player.room % 4 == 0:

            shop(player)

    # --------------------------------------------------------
    # Boss
    # --------------------------------------------------------

    result = boss_chamber(player)

    if result:

        player.score += 2000

        victory(player)

    else:

        if player.lives <= 0:

            game_over(player)

        else:

            clear()

            print(
                color(
                    "The Riddle Master laughs...",
                    RED
                )
            )

            print()

            print(
                "You were close."
            )

            print(
                f"Final score: {player.score}"
            )

            pause()


# ============================================================
#                       START GAME
# ============================================================

if __name__ == "__main__":
    main()
