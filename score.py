from turtle import Turtle


MAX_SCORE = 600
ALIGNMENT = "center"
FONT_SCORE = ("Courier", 17, "normal")
FONT_MESSAGE = ("Courier", 30, "normal")
FONT_HIGHSCORE = ("Courier", 25, "normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()

        self.value = 0
        self.highscore = 0

        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.write(0)


    def check_win(self):
        if self.value == MAX_SCORE:
            self.game_won()
            return True
        return False


    def write(self, add_score):
        self.clear()
        self.value += add_score
        super().write(f"Score = {self.value}", move = False, align = ALIGNMENT, font = FONT_SCORE)


    def game_over(self):
        self.goto(0, 0)
        super().write(f"GAME OVER", move = False, align = ALIGNMENT, font = FONT_MESSAGE)
        self.highscore_print()


    def game_won(self):
        self.goto(0, 0)
        super().write(f"YOU WIN", move = False, align = ALIGNMENT, font = FONT_MESSAGE)
        self.highscore_print()


    def highscore_print(self):
        if self.highscore < self.value:
            self.highscore = self.value
        self.goto(0, -30)
        super().write(f"HighScore = {self.highscore}", move = False, align = ALIGNMENT, font = FONT_HIGHSCORE)


    def reset(self):
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        
        self.value = 0
        self.write(0)


