from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scorecard import Scorecard
screen = Screen()
screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("My Snake")
screen.tracer(0)
snake = Snake()
snake.create_snake()
food = Food()
scorecard = Scorecard()
game_is_on = True

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.new_segment[0].distance(food) < 15:
        snake.add_snake()
        scorecard.increase_score()
        food.refresh()

    # Detect Collision with wall
    if snake.new_segment[0].xcor() > 285 or snake.new_segment[0].xcor() < -285 or snake.new_segment[0].ycor() > 280 \
            or snake.new_segment[0].ycor() < -280:
        scorecard.reset()
        snake.reset()
        scorecard.game_over()
        game_is_on = False
    # for _ in snake.new_segment:
    #     if _ == snake.new_segment[0]:
    #         pass
    #     elif snake.new_segment[0].distance(_) < 10:
    #         game_is_on = False
    #         scorecard.game_over()

    # Detect Collision with tail
    new_seg = snake.new_segment[1:]
    for seg in new_seg:
        if snake.new_segment[0].distance(seg) < 10:
            scorecard.reset()
            snake.reset()
            scorecard.game_over()
            game_is_on = False
screen.exitonclick()