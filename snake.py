
from turtle import Turtle
import random

STARTING_POSITION = [(-40,0), (-20,0), (0,0)]
MOVE_DISTANCE = 20
SNAKE_COLOR = "white"
SCREEN_LIMIT = 280
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.head_heading = RIGHT
        self.create_snake()


    def create_snake(self):
        for position in STARTING_POSITION:
            self.create_new_segment(position)


    def create_new_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color(SNAKE_COLOR)
        new_segment.penup()
        new_segment.goto(position)
        self.segments.insert(0, new_segment)


    def move(self, food_eated):
        self.create_new_segment(self.segments[0].pos())
        self.segments[0].setheading(self.head_heading)
        self.segments[0].forward(MOVE_DISTANCE)

        if not food_eated:
            self.segments[-1].hideturtle()
            del self.segments[-1]
    

    def up(self):
        if self.head_heading != DOWN:
            self.head_heading = UP
            self.segments[-1].setheading(UP)


    def down(self):
        if self.head_heading != UP:
            self.head_heading = DOWN
            self.segments[-1].setheading(DOWN)


    def left(self):
        if self.head_heading != RIGHT:
            self.head_heading = LEFT
            self.segments[-1].setheading(LEFT)


    def right(self):
        if self.head_heading != LEFT:
            self.head_heading = RIGHT
            self.segments[-1].setheading(RIGHT)


    def hit_something(self):
        if abs(self.segments[0].pos()[0]) > SCREEN_LIMIT:
            return True
        
        if abs(self.segments[0].pos()[1]) > SCREEN_LIMIT:
            return True
        
        for current in self.segments[1:]:
            if self.segments[0].pos() == current.pos():
                return True
            
        return False
    
    def reset(self):
        self.__init__()
    

