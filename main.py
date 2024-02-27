from snake import Snake
from food import Food
from score import Score
from turtle import Screen
import os

os.system("clear")

FOOD_EATED = 1
FOOD_NOT_EATED = 0
DIFICULTY = 200  # ms per step

WIDTH = 600
HEIGHT = 600

game_is_on = True

game_screen = Screen()
game_screen.setup(width = WIDTH, height = HEIGHT)
game_screen.bgcolor("black")
game_screen.title("Snake Game")
game_screen.tracer(0)
game_screen.listen()

score = Score()
snake = Snake()
food = Food()


def game_loop():
  
  if food.eated(snake.segments[0]):
    snake.move(FOOD_EATED)
    food.add_food(snake.segments)
    score.write(1)
  else:
    snake.move(FOOD_NOT_EATED) 

  if snake.hit_something():
    score.game_over()
    return 

  if score.check_win():
    return 
  
  game_screen.update()
  game_screen.ontimer(game_loop, DIFICULTY) 



while game_is_on:
    
  game_screen.onkey(fun = snake.up, key = "Up")
  game_screen.onkey(fun = snake.down, key = "Down")
  game_screen.onkey(fun = snake.left, key = "Left")
  game_screen.onkey(fun = snake.right, key = "Right")

  game_loop()

  if input("Do you want to play again? YES / NO -> ").lower() != "yes":
    break

  game_screen.clear()
  game_screen.bgcolor("black")
  game_screen.tracer(0)
  game_screen.listen()
  snake.reset()
  food.reset()
  score.reset()

game_screen.exitonclick()

                    
