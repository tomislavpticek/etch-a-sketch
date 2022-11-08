class EtchASketch:

    def __init__(self, turtle, screen):
        self.turtle = turtle
        self.screen = screen

    def forward(self):
        self.turtle.forward(10)

    def backward(self):
        self.turtle.backward(10)

    def left(self):
        self.turtle.left(5)

    def right(self):
        self.turtle.right(5)

    def clear(self):
        self.turtle.clear()

    def reset_position(self):
        self.turtle.penup()
        self.turtle.home()
        self.turtle.pendown()
