from tkinter import *
import random

GAME_WIDTH = 1000
GAME_HEIGHT = 500
SPEED = 60
SPACE_SIZE = 20
BODY_PARTS = 3
SNAKE_COLOR = "#0000FF"
FOOD_COLOR = "#FFFF00"
BACKGROUND_COLOR = "#000000"

class Snake(object):
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = [] 

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food(object):
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")

def next_turn(snake, food):
    global direction
    global SPEED
    global score

    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)
    snake.squares.insert(0, square)

    # ✅ Check for collisions
    if check_collision(snake):
        game_over()
        return

    # Check if snake eats food
    if x == food.coordinates[0] and y == food.coordinates[1]:
        score += 1
        label.config(text=f"Score: {score}")
        
        canvas.delete("food")
        food = Food()

        # Speed up every 10 points
        if score % 10 == 0 and SPEED > 30:
            SPEED -= 5
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    window.after(SPEED, next_turn, snake, food)

def change_direction(event):
    global direction
    key = event.keysym

    if key == "Up" and direction != "down":
        direction = "up"
    elif key == "Down" and direction != "up":
        direction = "down"
    elif key == "Left" and direction != "right":
        direction = "left"
    elif key == "Right" and direction != "left":
        direction = "right"

def check_collision(snake):
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        return True

    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            return True

    return False

def game_over():
    canvas.delete(ALL)
    canvas.create_text(
        GAME_WIDTH / 2,
        GAME_HEIGHT / 2,
        font=("consolas", 70),
        text="GAME OVER",
        fill="red",
        tag="gameover"
    )

# --- Main Program ---
window = Tk()
window.title("Snake Game")
window.resizable(False, False)

score = 0
direction = 'down'  # default starting direction

label = Label(window, text="Score: {}".format(score), font=("consolas", 40))
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 2) - (window_width / 2))
y = int((screen_height / 2) - (window_height / 2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Bind key events
window.bind("<Up>", change_direction)
window.bind("<Down>", change_direction)
window.bind("<Left>", change_direction)
window.bind("<Right>", change_direction)

# Start game
snake = Snake()
food = Food()
next_turn(snake, food)

window.mainloop()
