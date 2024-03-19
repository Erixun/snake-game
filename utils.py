from collections import namedtuple
from turtle import _Screen, Screen
from snake import Snake


def bind_keys(screen: _Screen, snake: Snake):
    if not isinstance(screen, _Screen):
        raise TypeError("Expected a turtle.Screen object")
    if not isinstance(snake, Snake):
        raise TypeError("Expected a Snake object")

    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")
    screen.listen()


def init_screen(snake: Snake):
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snekky")
    screen.tracer(0)
    bind_keys(screen, snake)

    return screen


coords = namedtuple("Coords", ["x", "y"])


def get_wall(screen: _Screen):
    x, y = screen.window_width() / 2, screen.window_height() / 2
    return coords(int(x - 10), int(y - 10))
