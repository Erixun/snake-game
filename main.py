from snake import Snake
from utils import init_screen

snake = Snake()
screen = init_screen(snake)

game_is_on = True
while game_is_on:
    screen.update()
    snake.move()


screen.exitonclick()
