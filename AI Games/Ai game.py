import random
import os
import time
import string

# ============================================================
#                    PUZZLE MASTER
#              The Ultimate Brain Challenge
# ============================================================

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


def c(text, colour):
    return f"{colour}{text}{RESET}"


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    input(c("\nPress ENTER to continue...", GRAY))


def type_text(text, delay=0.015):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


# ============================================================
#                         PLAYER
# ============================================================

class Player:

    def __init__(self):
        self.score = 0
        self.streak = 0
        self.best_streak = 0
        self.lives = 3
        self.level = 1
        self.hints = 3

    def correct(self, points):
        self.streak += 1

        self.best_streak = max(
            self.best_streak,
            self.streak
        )

        bonus = self.streak * 5

        self.score += points + bonus

        print(
            c(
                f"\n✓ CORRECT! +{points + bonus} points",
                GREEN
            )
        )

        print(
            c(
                f"Streak bonus: +{bonus}",
                YELLOW
            )
        )

    def wrong(self):
        self.streak = 0
        self.lives -= 1

        print(
            c(
                "\n✗ WRONG!",
                RED
            )
        )

        print(
            c(
                f"Lives remaining: {self.lives}",
                YELLOW
            )
        )


# ============================================================
#                       GAME HEADER
# ============================================================

def header(player, title):

    print(
        c(
            "╔" + "═" * 60 + "╗",
            CYAN
        )
    )

    print(
        c(
            f"║ {title:^58} ║",
            BOLD
        )
    )

    print(
        c(
            "╠" + "═" * 60 + "╣",
            CYAN
        )
    )

    print(
        f"  Level: {player.level}"
        f"    Score: {player.score}"
        f"    Lives: {player.lives}"
        f"    Hints: {player.hints}"
    )

    print(
        c(
            "╚" + "═" * 60 + "╝",
            CYAN
        )
    )

    print()


# ============================================================
#                         HINT
# ============================================================

def use_hint(player, hint):

    if player.hints <= 0:

        print(
            c(
                "You have no hints left!",
                RED
            )
        )

        return False

    choice = input(
        "\nUse a hint? (y/n): "
    ).lower()

    if choice == "y":

        player.hints -= 1

        print(
            c(
                f"\nHINT: {hint}",
                YELLOW
            )
        )

        return True

    return False


# ============================================================
#                 PUZZLE 1: NUMBER SEQUENCE
# ============================================================

def number_sequence(player):

    clear()

    header(
        player,
        "PUZZLE 1 - NUMBER SEQUENCE"
    )

    patterns = [

        ([2, 4, 6, 8], 10,
         "Add 2 each time."),

        ([3, 6, 12, 24], 48,
         "Each number is multiplied by 2."),

        ([5, 10, 20, 40], 80,
         "Each number is doubled."),

        ([1, 4, 9, 16], 25,
         "These are square numbers."),

        ([2, 6, 12, 20], 30,
         "Look at the differences: 4, 6, 8..."),

        ([100, 90, 80, 70], 60,
         "Subtract 10 each time."),

        ([1, 1, 2, 3, 5, 8], 13,
         "Each number is the sum of the previous two.")

    ]

    sequence, answer, hint = random.choice(patterns)

    print(
        "What number comes next?"
    )

    print()

    print(
        c(
            "   " + " → ".join(
                str(x) for x in sequence
            ) + " → ?",
            YELLOW
        )
    )

    print()

    use_hint(
        player,
        hint
    )

    try:

        guess = int(
            input("\nAnswer: ")
        )

    except ValueError:

        guess = -999

    if guess == answer:

        player.correct(100)
        pause()
        return True

    player.wrong()

    print(
        f"The answer was {answer}."
    )

    pause()

    return False


# ============================================================
#                 PUZZLE 2: WORD SCRAMBLE
# ============================================================

def word_scramble(player):

    clear()

    header(
        player,
        "PUZZLE 2 - WORD SCRAMBLE"
    )

    words = [
        "PYTHON",
        "PUZZLE",
        "COMPUTER",
        "MYSTERY",
        "ROCKET",
        "GALAXY",
        "DRAGON",
        "THUNDER",
        "SHADOW",
        "TREASURE",
        "DIAMOND",
        "ADVENTURE"
    ]

    word = random.choice(words)

    scrambled = list(word)

    random.shuffle(scrambled)

    scrambled = "".join(scrambled)

    # Ensure it isn't accidentally identical
    while scrambled == word:

        scrambled = list(word)
        random.shuffle(scrambled)
        scrambled = "".join(scrambled)

    print(
        "Unscramble this word:"
    )

    print()

    print(
        c(
            f"        {scrambled}",
            MAGENTA
        )
    )

    print()

    guess = input(
        "Answer: "
    ).strip().upper()

    if guess == word:

        player.correct(100)
        pause()
        return True

    player.wrong()

    print(
        f"The answer was {word}."
    )

    pause()

    return False


# ============================================================
#                 PUZZLE 3: MEMORY
# ============================================================

def memory_puzzle(player):

    clear()

    header(
        player,
        "PUZZLE 3 - MEMORY"
    )

    symbols = [
        "◆",
        "●",
        "▲",
        "■",
        "★",
        "♥",
        "☀",
        "♦"
    ]

    sequence = random.sample(
        symbols,
        5
    )

    print(
        "Memorize this sequence:"
    )

    print()

    print(
        c(
            "  " + " ".join(sequence),
            YELLOW
        )
    )

    time.sleep(3)

    clear()

    header(
        player,
        "PUZZLE 3 - MEMORY"
    )

    print(
        "What was the sequence?"
    )

    print()

    guess = input(
        "Enter the symbols in order: "
    ).strip()

    answer = "".join(sequence)

    cleaned = guess.replace(
        " ",
        ""
    )

    if cleaned == answer:

        player.correct(150)
        pause()
        return True

    player.wrong()

    print(
        "The sequence was:"
    )

    print(
        " ".join(sequence)
    )

    pause()

    return False


# ============================================================
#                 PUZZLE 4: CODE BREAKER
# ============================================================

def code_breaker(player):

    clear()

    header(
        player,
        "PUZZLE 4 - CODE BREAKER"
    )

    numbers = [
        random.randint(1, 9)
        for _ in range(4)
    ]

    # Make digits unique
    while len(set(numbers)) != 4:

        numbers = [
            random.randint(1, 9)
            for _ in range(4)
        ]

    secret = "".join(
        str(x) for x in numbers
    )

    print(
        "Crack the 4-digit code."
    )

    print()

    print(
        c(
            "Each digit is between 1 and 9.",
            GRAY
        )
    )

    print()

    attempts = 5

    while attempts > 0:

        print(
            f"Attempts remaining: {attempts}"
        )

        guess = input(
            "Code: "
        ).strip()

        if len(guess) != 4 or not guess.isdigit():

            print(
                c(
                    "Enter exactly 4 digits.",
                    RED
                )
            )

            continue

        if guess == secret:

            player.correct(200)
            pause()
            return True

        correct_position = 0
        correct_digit = 0

        for i in range(4):

            if guess[i] == secret[i]:

                correct_position += 1

            elif guess[i] in secret:

                correct_digit += 1

        print(
            c(
                f"Correct position: "
                f"{correct_position}",
                GREEN
            )
        )

        print(
            c(
                f"Correct digit, wrong position: "
                f"{correct_digit}",
                YELLOW
            )
        )

        attempts -= 1

    player.wrong()

    print(
        f"The code was {secret}."
    )

    pause()

    return False


# ============================================================
#                 PUZZLE 5: LOGIC
# ============================================================

def logic_puzzle(player):

    clear()

    header(
        player,
        "PUZZLE 5 - LOGIC"
    )

    print(
        "Three friends — Alex, Blake and Casey —"
    )

    print(
        "each have a different favorite color:"
    )

    print()

    print(
        "Red, Blue and Green."
    )

    print()

    print(
        "Clues:"
    )

    print(
        "1. Alex does not like Red."
    )

    print(
        "2. Blake likes neither Red nor Green."
    )

    print(
        "3. Casey does not like Green."
    )

    print()

    print(
        "What color does Alex like?"
    )

    print(
        "\n1. Red"
        "\n2. Blue"
        "\n3. Green"
    )

    answer = input(
        "\nAnswer: "
    ).strip()

    if answer == "3":

        player.correct(200)
        pause()
        return True

    player.wrong()

    print(
        "The answer is Green."
    )

    pause()

    return False


# ============================================================
#                 PUZZLE 6: MATH
# ============================================================

def math_puzzle(player):

    clear()

    header(
        player,
        "PUZZLE 6 - MATH CHALLENGE"
    )

    a = random.randint(
        10,
        30
    )

    b = random.randint(
        5,
        20
    )

    c_num = random.randint(
        2,
        10
    )

    operations = [
        ("+", a + b + c_num),
        ("-", a - b * c_num),
        ("*", a * b + c_num)
    ]

    operation, answer = random.choice(
        operations
    )

    if operation == "+":

        question = (
            f"{a} + {b} + {c_num}"
        )

    elif operation == "-":

        question = (
            f"{a} - {b} × {c_num}"
        )

    else:

        question = (
            f"{a} × {b} + {c_num}"
        )

    print(
        f"Solve:"
    )

    print()

    print(
        c(
            f"        {question} = ?",
            YELLOW
        )
    )

    print()

    try:

        guess = int(
            input("Answer: ")
        )

    except ValueError:

        guess = -999

    if guess == answer:

        player.correct(150)
        pause()
        return True

    player.wrong()

    print(
        f"The answer was {answer}."
    )

    pause()

    return False


# ============================================================
#                 PUZZLE 7: ODD ONE OUT
# ============================================================

def odd_one_out(player):

    clear()

    header(
        player,
        "PUZZLE 7 - ODD ONE OUT"
    )

    groups = [

        (
            ["APPLE", "BANANA", "ORANGE", "CARROT"],
            "CARROT"
        ),

        (
            ["DOG", "CAT", "HORSE", "EAGLE"],
            "EAGLE"
        ),

        (
            ["RED", "BLUE", "GREEN", "CIRCLE"],
            "CIRCLE"
        ),

        (
            ["2", "4", "6", "9"],
            "9"
        ),

        (
            ["MARS", "EARTH", "JUPITER", "MOON"],
            "MOON"
        )

    ]

    group, answer = random.choice(
        groups
    )

    random.shuffle(group)

    print(
        "Which item doesn't belong?"
    )

    print()

    for i, item in enumerate(
        group,
        1
    ):

        print(
            f"{i}. {item}"
        )

    print()

    try:

        choice = int(
            input("Number: ")
        )

        selected = group[
            choice - 1
        ]

    except:

        selected = ""

    if selected == answer:

        player.correct(150)
        pause()
        return True

    player.wrong()

    print(
        f"The answer was {answer}."
    )

    pause()

    return False


# ============================================================
#                 PUZZLE 8: WORD LOGIC
# ============================================================

def word_logic(player):

    clear()

    header(
        player,
        "PUZZLE 8 - WORD LOGIC"
    )

    print(
        "What word comes next?"
    )

    print()

    print(
        c(
            "CAT → CATS",
            YELLOW
        )
    )

    print(
        c(
            "DOG → DOGS",
            YELLOW
        )
    )

    print(
        c(
            "BIRD → BIRDS",
            YELLOW
        )
    )

    print()

    print(
        "What does:"
    )

    print(
        c(
            "FOX → ?",
            MAGENTA
        )
    )

    answer = input(
        "\nAnswer: "
    ).strip().upper()

    if answer == "FOXS" or answer == "FOXES":

        player.correct(100)
        pause()
        return True

    player.wrong()

    print(
        "The intended answer was FOXES."
    )

    pause()

    return False


# ============================================================
#                 PUZZLE 9: PATTERN
# ============================================================

def pattern_puzzle(player):

    clear()

    header(
        player,
        "PUZZLE 9 - PATTERN MASTER"
    )

    patterns = [

        (
            "A C E G ?",
            "I",
            "Skip one letter each time."
        ),

        (
            "1 3 6 10 ?",
            "15",
            "Add 2, then 3, then 4..."
        ),

        (
            "2 4 8 16 ?",
            "32",
            "Double each time."
        ),

        (
            "Z X V T ?",
            "R",
            "Move backward by 2 letters."
        )

    ]

    question, answer, hint = random.choice(
        patterns
    )

    print(
        c(
            question,
            YELLOW
        )
    )

    print()

    use_hint(
        player,
        hint
    )

    guess = input(
        "\nAnswer: "
    ).strip().upper()

    if guess == answer:

        player.correct(200)
        pause()
        return True

    player.wrong()

    print(
        f"The answer was {answer}."
    )

    pause()

    return False


# ============================================================
#                 FINAL PUZZLE
# ============================================================

def final_puzzle(player):

    clear()

    header(
        player,
        "FINAL PUZZLE - THE MASTER LOCK"
    )

    type_text(
        "You have reached the final door..."
    )

    type_text(
        "Four locks stand between you and victory."
    )

    print()

    time.sleep(1)

    # Lock 1
    print(
        c(
            "LOCK 1",
            RED
        )
    )

    print(
        "What is 12 × 3?"
    )

    try:

        answer = int(
            input("> ")
        )

    except:

        answer = -1

    if answer != 36:

        return False

    print(
        c(
            "LOCK 1 OPEN",
            GREEN
        )
    )

    # Lock 2
    print()

    print(
        c(
            "LOCK 2",
            RED
        )
    )

    print(
        "Complete:"
    )

    print(
        "2, 4, 8, 16, ?"
    )

    answer = input(
        "> "
    ).strip()

    if answer != "32":

        return False

    print(
        c(
            "LOCK 2 OPEN",
            GREEN
        )
    )

    # Lock 3
    print()

    print(
        c(
            "LOCK 3",
            RED
        )
    )

    print(
        "Which is different?"
    )

    print(
        "APPLE  BANANA  POTATO  ORANGE"
    )

    answer = input(
        "> "
    ).strip().upper()

    if answer != "POTATO":

        return False

    print(
        c(
            "LOCK 3 OPEN",
            GREEN
        )
    )

    # Lock 4
    print()

    print(
        c(
            "LOCK 4",
            RED
        )
    )

    print(
        "Unscramble:"
    )

    print(
        c(
            "R E T A W",
            MAGENTA
        )
    )

    answer = input(
        "> "
    ).strip().upper()

    if answer != "WATER":

        return False

    print(
        c(
            "LOCK 4 OPEN",
            GREEN
        )
    )

    time.sleep(1)

    player.score += 1000

    return True


# ============================================================
#                       GAME OVER
# ============================================================

def game_over(player):

    clear()

    print(
        c(
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
        f"Final Score: {player.score}"
    )

    print(
        f"Best Streak: {player.best_streak}"
    )

    print(
        f"Level Reached: {player.level}"
    )

    pause()


# ============================================================
#                       VICTORY
# ============================================================

def victory(player):

    clear()

    print(
        c(
            """
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
        c(
            "YOU HAVE DEFEATED THE PUZZLE MASTER!",
            YELLOW
        )
    )

    print()

    print(
        f"Final Score: {player.score}"
    )

    print(
        f"Best Streak: {player.best_streak}"
    )

    print(
        f"Remaining Lives: {player.lives}"
    )

    print()

    print(
        c(
            "Your brain is officially dangerous.",
            MAGENTA
        )
    )

    pause()


# ============================================================
#                         MAIN
# ============================================================

def main():

    clear()

    print(
        c(
            "╔══════════════════════════════════════════════════════════╗",
            CYAN
        )
    )

    print(
        c(
            "║                    PUZZLE MASTER                       ║",
            BOLD
        )
    )

    print(
        c(
            "║              THE ULTIMATE BRAIN TEST                   ║",
            CYAN
        )
    )

    print(
        c(
            "╚══════════════════════════════════════════════════════════╝",
            CYAN
        )
    )

    print()

    print(
        "Can you beat all 10 puzzles?"
    )

    print(
        "You have 3 lives."
    )

    print(
        "Use your hints carefully."
    )

    print()

    input(
        "Press ENTER to begin..."
    )

    player = Player()

    puzzles = [
        number_sequence,
        word_scramble,
        memory_puzzle,
        code_breaker,
        logic_puzzle,
        math_puzzle,
        odd_one_out,
        word_logic,
        pattern_puzzle
    ]

    for i, puzzle in enumerate(
        puzzles,
        1
    ):

        player.level = i

        result = puzzle(player)

        if player.lives <= 0:

            game_over(player)
            return

    # Final level
    player.level = 10

    clear()

    print(
        c(
            "YOU HAVE REACHED THE FINAL CHALLENGE.",
            MAGENTA
        )
    )

    print()

    pause()

    result = final_puzzle(player)

    if result:

        victory(player)

    else:

        print(
            c(
                "\nYou failed the Master Lock.",
                RED
            )
        )

        print(
            "The door remains closed..."
        )

        pause()


if __name__ == "__main__":
    main()
