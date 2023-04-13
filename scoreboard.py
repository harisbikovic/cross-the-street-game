from turtle import Turtle

FONT = ("Arial", 20, "normal")
GAME_OVER = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.setposition(250, 260)
        self.write(f"Level: {self.level}", False, "right", FONT)

    def update(self):
        self.clear()
        self.level += 1
        self.write(f"Level {self.level}", False, "right", FONT)

    def game_over(self):
        game_over = Turtle()
        game_over.hideturtle()
        game_over.penup()
        game_over.setposition(0, 0)
        game_over.write("GAME OVER", False, "center", GAME_OVER)
