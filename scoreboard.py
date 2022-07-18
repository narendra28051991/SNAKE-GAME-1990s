from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.high_score = 0
        with open("data.txt") as data:
            self.score = int(data.read())
        self.create_scoreboard()

    def create_scoreboard(self):
        self.color("white")
        self.penup()
        self.goto(0, 250)
        self.print_score()
        self.hideturtle()

    def update_score(self):
        self.score += 1
        self.print_score()

    def print_score(self):
        self.clear()
        self.write(f"Score: {self.score} High-score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.print_score()