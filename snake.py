import time
from turtle import Turtle

UP, DOWN, LEFT, RIGHT = 90, 270, 180, 0


class SnakePiece(Turtle):
    def __init__(self, index):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.goto(-20 * index, 0)
        self.ahead: SnakePiece = None

    def move(self):
        #TODO: handle edge
        self.goto(self.ahead.pos()) if self.ahead else self.forward(20)

    def set_ahead(self, piece):
        self.ahead = piece


class Snake:
    def __init__(self, segments=4):
        self.body = self.init_snake(segments)
        self.head = self.body[0]
        self.tail = self.body[-1]
        self.speed = 0.05

    def init_snake(self, length) -> list[SnakePiece]:
        snake_body = []
        for n in range(length):
            piece = SnakePiece(n)
            piece.set_ahead(snake_body[n - 1] if n > 0 else None)
            snake_body.append(piece)

        return snake_body

    def extend(self):
        piece = SnakePiece(len(self.body))
        piece.set_ahead(self.body[-1])
        piece.goto(self.tail.pos())
        self.body.append(piece)
        self.tail = piece

    def move(self):
        for piece in reversed(self.body):
            piece.move()
            time.sleep(self.speed)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
