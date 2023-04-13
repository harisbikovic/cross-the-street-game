import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
SLEEP_TIME = 0.1

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(SLEEP_TIME)
    screen.update()
    if car_manager.counter % 6 == 0 and car_manager.counter != 0:
        car_manager.create_car()    # Create a car on every 6th utterance
        car_manager.counter = 0
    car_manager.counter_increment()

    # Collision with cars
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Turtle reaches finish line
    if player.ycor() > player.finish_line():
        player.start_new_level()
        scoreboard.update()
        SLEEP_TIME *= 0.5    # Increase the speed of cars

screen.exitonclick()
