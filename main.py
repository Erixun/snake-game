from food import Food
from score import ScoreBoard
from snake import Snake
from utils import get_wall, init_screen

snake = Snake()
food = Food()
score_board = ScoreBoard()
screen = init_screen(snake)
wall = get_wall(screen)

game_is_on = True
while game_is_on:
    screen.update()
    snake.move()

    if snake.head.distance(food) < 15:
        snake.extend()
        snake.speed *= 0.9
        score_board.increase_score()
        food.place_randomly()

    if snake.collide(snake, wall):
        game_is_on = False
        score_board.game_over()

screen.exitonclick()
