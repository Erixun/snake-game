from food import Food
from snake import Snake
from utils import init_screen

snake = Snake()
screen = init_screen(snake)
food = Food()
game_is_on = True
while game_is_on:
    screen.update()
    snake.move()

    if snake.head.distance(food) < 15:
        snake.extend()
        snake.speed *= 0.9
        food.place_randomly()


screen.exitonclick()
