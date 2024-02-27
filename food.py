
from turtle import Turtle
import random

MARGINS_LEFT_X = -280
MARGINS_RIGHT_X = 280

MARGINS_DOWN_Y = -280
MARGINS_UP_Y = 280

STEP = 20


class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("red")
        self.add_food([])


    def add_food(self, segments):
        self.goto(random.randrange(MARGINS_LEFT_X, MARGINS_RIGHT_X + 1, STEP), random.randrange(MARGINS_DOWN_Y, MARGINS_UP_Y + 1, STEP))
        for current in segments:
            if current.pos() == self.pos():
                self.add_food(segments)


    def eated(self, snake_head):
        if snake_head.pos() == self.pos():
            return True
        else:
            return False
    

    def reset(self):
        self.__init__()
