from turtle import Turtle
# DEFINE
ALIGNMENT = "center"
FONT = ("Georgia", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("Pink")  # should do before write
        self.penup()        #get rid of the line when we move the scoreboard up
        self.goto(0, 270)
        self.hideturtle()   # get rid of the arrow of turtle
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font= FONT)

    def increase_score(self):
        self.score += 1
        self.clear()    # clear the previous text was written (scoreboard)
        self.update_scoreboard()

    def gameOver(self):
        self.goto(0,0)      # Center
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

