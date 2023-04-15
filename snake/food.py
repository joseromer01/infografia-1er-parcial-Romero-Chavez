import arcade
import random

class Food:
    SIZE = 20

    def __init__(self):
        self.position = self.random_position()

    def draw(self):
        x, y = self.position
        arcade.draw_rectangle_filled(x, y, self.SIZE, self.SIZE, arcade.color.RED)

    def move(self):
        self.position = self.random_position()

    def random_position(self):
        x = random.randrange(self.SIZE, arcade.get_window().width - self.SIZE, self.SIZE)
        y = random.randrange(self.SIZE, arcade.get_window().height - self.SIZE, self.SIZE)
        return x, y

