import arcade

class Snake:
    MOVE_DISTANCE = 4

    def __init__(self):
        self.segments = [(0, 0), (20, 0), (40, 0)]
        self.direction = arcade.key.RIGHT
        self.grow = 0
        self.dead = False

    def draw(self):
        for x, y in self.segments:
            arcade.draw_rectangle_filled(x, y, 20, 20, arcade.color.PURPLE
                                         )

    def move(self):
        if self.dead:
            return

        x, y = self.segments[-1]
        if self.direction == arcade.key.UP:
            y += self.MOVE_DISTANCE
        elif self.direction == arcade.key.DOWN:
            y -= self.MOVE_DISTANCE
        elif self.direction == arcade.key.LEFT:
            x -= self.MOVE_DISTANCE
        elif self.direction == arcade.key.RIGHT:
            x += self.MOVE_DISTANCE

        if self.hits_wall(x, y):
           self.dead = True
           print("Game over!")
           return

        if self.hits_self(x, y):
            self.dead = True
            print("Game over!")
            return

        self.segments.append((x, y))
        if self.grow == 0:
            self.segments.pop(0)
        else:
            self.grow -= 1

    def hits_self(self, x, y):
        for segment in self.segments[:-1]:
            if segment == (x, y):
                return True
        return False
    
    def hits_wall(self, x, y):
        if x < 0 or x > 620 or y < 0 or y > 460:
            return True
        return False

    def eats(self, food):
        head = self.segments[-1]
        if head == food.position:
            self.grow += 1
            return True
        return False

    def on_key_press(self, key, modifiers):
        if key in [arcade.key.UP, arcade.key.DOWN, arcade.key.LEFT, arcade.key.RIGHT]:
            if key != self.opposite_direction():
                self.direction = key

    def opposite_direction(self):
        if self.direction == arcade.key.UP:
            return arcade.key.DOWN
        elif self.direction == arcade.key.DOWN:
            return arcade.key.UP
        elif self.direction == arcade.key.LEFT:
            return arcade.key.RIGHT
        elif self.direction == arcade.key.RIGHT:
            return arcade.key.LEFT
        
        

