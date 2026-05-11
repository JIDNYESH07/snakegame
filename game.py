import turtle
import time
import random
# game by jidnyesh patil 
delay = 0.1
score = 0
high_score = 0

# Set up the screen
wn = turtle.Screen()
wn.title("snake game by @Jidnyesh")
wn.bgcolor("black")
wn.setup(width=700, height=700)
wn.tracer(0)

# Snake head
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("blue")
head.penup()
head.goto(0, 0)
head.direction = "stop"
head.hideturtle()

# Snake food
food = turtle.Turtle()
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)
food.hideturtle()

segments = []

# Pen
pen = turtle.Turtle()
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)

# Colored title letters S-N-A-K-E  G-A-M-E
title_pen = turtle.Turtle()
title_pen.penup()
title_pen.hideturtle()

# Letter colors: S=red, N=blue, A=green, K=orange, E=purple, G=red, A=orange, M=blue, E=grey
letters = [
    ("S", "red"),
    ("N", "blue"),
    ("A", "green"),
    ("K", "orange"),
    ("E", "purple"),
    (" ", "white"),
    ("G", "red"),
    ("A", "orange"),
    ("M", "blue"),
    ("E", "grey")
]

# Calculate start x position to center the title
start_x = -200
y_pos = 50

for i, (letter, color) in enumerate(letters):
    title_pen.goto(start_x + i * 40, y_pos)
    title_pen.color(color)
    title_pen.write(letter, align="center", font=("courier", 36, "bold"))

# by @Jidnyesh line
title_pen.goto(0, -20)
title_pen.color("white")
title_pen.write("by @Jidnyesh", align="center", font=("courier", 18, "normal"))

# Start screen
start_pen = turtle.Turtle()
start_pen.color("white")
start_pen.penup()
start_pen.hideturtle()
start_pen.goto(0, -100)
start_pen.write("Press SPACE to Start", align="center", font=("courier", 20, "normal"))
start_pen.goto(0, -150)
start_pen.write("Move: W A S D", align="center", font=("courier", 16, "normal"))

game_started = False

# Functions
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

def start_game():
    global game_started
    if not game_started:
        game_started = True
        start_pen.clear()
        title_pen.clear()           # clear colored title
        head.showturtle()
        food.showturtle()
        pen.write("Score:0  High Score:0", align="center", font=("courier", 24, "normal"))

def reset_game():
    global score, delay
    time.sleep(1)
    head.goto(0, 0)
    head.direction = "stop"
    for seg in segments:
        seg.goto(1000, 1000)
    segments.clear()
    score = 0
    delay = 0.1
    pen.clear()
    pen.write("Score:{}  High Score:{}".format(score, high_score), align="center", font=("courier", 24, "normal"))

# Keyboard binding
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(start_game, "space")

# Main game loop
while True:
    wn.update()

    if not game_started:
        continue

    # Check for collision with border
    if head.xcor() > 340 or head.xcor() < -340 or head.ycor() > 340 or head.ycor() < -340:
        reset_game()

    # Check for a collision with the food
    if head.distance(food) < 20:
        food.goto(random.randint(-340, 340), random.randint(-340, 340))
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score:{}  High Score:{}".format(score, high_score), align="center", font=("courier", 24, "normal"))

    # Move the end segment first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move segment 0 to where head is
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)

    move()

    # Check for collision with body segments
    for segment in segments:
        if segment.distance(head) < 20:
            reset_game()

    time.sleep(delay)

wn.mainloop()