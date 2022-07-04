from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

is_game_running = True

screen_game = Screen()
screen_game.setup(width=600,height=600)
screen_game.bgcolor("black")
screen_game.title("Snake Game!")
screen_game.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen_game.listen()
screen_game.onkey(snake.up, "Up")
screen_game.onkey(snake.down, "Down")
screen_game.onkey(snake.left, "Left")
screen_game.onkey(snake.right, "Right")

while is_game_running:
    screen_game.update()
    time.sleep(0.1)
    snake.move()

    #Detected food colision
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        snake.extends()
        food.refresh()

    #Detect wall colision
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.game_over()
        is_game_running = False

    #Detect nail colision
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            is_game_running = False



screen_game.exitonclick()