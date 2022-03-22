from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        with open("data.txt", mode="r") as data:
            self.high_Score = int(data.read())
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score : {self.high_Score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > int(self.high_Score):
            self.high_Score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.update_scoreboard()

    def add_score(self):
        self.score += 1
        self.update_scoreboard()
