from turtle import Turtle
ALIGN = "center"
FONT = ("Ariel", 22, "normal")
class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.penup()
        self.color("white")
        self.shapesize(10, 10)
        self.goto(x=0, y=270)
        self.hideturtle()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGN, font=FONT)

    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write("GAME OVER", align=ALIGN, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.clear()
        self.write(f"Game Over.", align="center", font=("Courier", 20, "normal"))