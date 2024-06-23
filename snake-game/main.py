import time
from snake import Snake
from turtle import Screen, Turtle
from food import Food
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snack Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()


# Key bindings
# Start listening for the keystrokes
screen.listen()
screen.onkey(snake.up, "Up" )
screen.onkey(snake.down, "Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right, "Right")

game_isOn = True
while game_isOn:
    screen.update()
    time.sleep(0.1)  # add 0.1s delay after all segments move
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 20: # Set distance for collision
        food.refresh()
        scoreboard.increase_score()

    # Detect collision with wall
    if (snake.head.xcor() > 290 or snake.head.xcor() < -290
            or snake.head.ycor() > 290 or snake.head.ycor() < -290):
        game_isOn = False
        scoreboard.gameOver()






screen.exitonclick()