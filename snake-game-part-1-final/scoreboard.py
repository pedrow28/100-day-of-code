from turtle import Turtle




class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.score = 0
        self.setposition(0, 280)
        self.refresh_score()

    def game_over(self):
        self.setposition(0, 0)
        self.write("GAME OVER", font=("Arial", 15, "normal"))

    def refresh_score(self):
        self.clear()
        self.write(f"Score: {self.score}", font=("Arial", 15, "normal"))
        self.score += 1
