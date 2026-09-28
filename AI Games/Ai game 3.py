import turtle
import random
import time

# -----------------------------
# Screen
# -----------------------------
screen = turtle.Screen()
screen.title("Dodge the Blocks")
screen.bgcolor("black")
screen.setup(width=600, height=700)
screen.tracer(0)

# -----------------------------
# Player
# -----------------------------
player = turtle.Turtle()
player.shape("square")
player.color("cyan")
player.penup()
player.goto(0, -300)

player_speed = 30

# -----------------------------
# Score
# -----------------------------
score = 0
game_over = False

score_display = turtle.Turtle()
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-280, 310)
score_display.write("Score: 0", font=("Arial", 18, "bold"))

# -----------------------------
# Player movement
# -----------------------------
def move_left():
    x = player.xcor()

    if x > -270:
        player.setx(x - player_speed)


def move_right():
    x = player.xcor()

    if x < 270:
        player.setx(x + player_speed)


screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

# -----------------------------
# Create falling blocks
# -----------------------------
blocks = []

def create_block():
    block = turtle.Turtle()
    block.shape("square")
    block.color(random.choice(["red", "orange", "yellow", "purple"]))
    block.penup()

    x = random.randint(-270, 270)
    y = 350

    block.goto(x, y)
    blocks.append(block)


# -----------------------------
# Collision detection
# -----------------------------
def collision(a, b):
    return (
        abs(a.xcor() - b.xcor()) < 30
        and abs(a.ycor() - b.ycor()) < 30
    )


# -----------------------------
# Game over screen
# -----------------------------
def show_game_over():
    message = turtle.Turtle()
    message.color("red")
    message.penup()
    message.hideturtle()
    message.goto(0, 30)

    message.write(
        "GAME OVER",
        align="center",
        font=("Arial", 35, "bold")
    )

    message.goto(0, -30)
    message.color("white")
    message.write(
        f"Score: {score}",
        align="center",
        font=("Arial", 20, "bold")
    )


# -----------------------------
# Main game
# -----------------------------
last_block_time = time.time()
block_delay = 0.7

while not game_over:
    screen.update()

    # Create new blocks
    if time.time() - last_block_time > block_delay:
        create_block()
        last_block_time = time.time()

    # Move blocks
    for block in blocks:
        block.sety(block.ycor() - 8)

        # Collision
        if collision(player, block):
            game_over = True

        # Block escaped
        if block.ycor() < -350:
            block.hideturtle()
            blocks.remove(block)

            score += 1

            score_display.clear()
            score_display.write(
                f"Score: {score}",
                font=("Arial", 18, "bold")
            )

    # Make game harder
    if score > 20:
        block_delay = 0.5

    if score > 40:
        block_delay = 0.35

    time.sleep(0.02)

# -----------------------------
# End game
# -----------------------------
show_game_over()

screen.mainloop()
