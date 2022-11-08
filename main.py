import turtle
from turtle import Turtle, Screen
from etch_a_sketch import EtchASketch

game = EtchASketch(Turtle(), Screen())

game.screen.listen()

game.screen.onkey(fun=game.forward, key="w")
game.screen.onkey(fun=game.backward, key="s")
game.screen.onkey(fun=game.left, key="a")
game.screen.onkey(fun=game.right, key="d")
game.screen.onkey(fun=game.clear, key="c")
game.screen.onkey(fun=game.reset_position, key="r")
game.screen.exitonclick()
