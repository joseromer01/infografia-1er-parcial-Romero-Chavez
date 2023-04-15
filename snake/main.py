import arcade
from snake import Snake
from food import Food

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
SCREEN_TITLE = "Snake Game"
BEST_SCORE = 0

class SnakeGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.SKY_BLUE)

        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_over = False
        self.showing_main_screen = True


    def on_draw(self):
        arcade.start_render()

        if self.showing_main_screen:
            arcade.draw_text("CRAZY SNAKE", SCREEN_WIDTH/2, SCREEN_HEIGHT/1.5, arcade.color.BLACK, font_size=50, anchor_x="center")
            arcade.draw_text("Presione ENTER para comenzar a jugar", SCREEN_WIDTH/2, SCREEN_HEIGHT/3, arcade.color.BLACK, font_size=20, anchor_x="center")

        else:
            arcade.draw_rectangle_filled(SCREEN_WIDTH/2, 0, SCREEN_WIDTH, 5, arcade.color.BLACK) # pared superior
            arcade.draw_rectangle_filled(SCREEN_WIDTH/2, SCREEN_HEIGHT, SCREEN_WIDTH, 5, arcade.color.BLACK) # pared inferior
            arcade.draw_rectangle_filled(0, SCREEN_HEIGHT/2, 10, SCREEN_HEIGHT, arcade.color.BLACK) # pared izquierda
            arcade.draw_rectangle_filled(SCREEN_WIDTH, SCREEN_HEIGHT/2, 10, SCREEN_HEIGHT, arcade.color.BLACK) # pared derecha

            if not self.snake.dead:
                self.snake.draw()
                self.food.draw()
                arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.BLACK, font_size=16)

            else:
                arcade.draw_text("GAME OVER!", SCREEN_WIDTH/2, SCREEN_HEIGHT/1.5, arcade.color.BLACK, font_size=70, anchor_x="center")
                arcade.draw_text("Apachurrale la barra espaciadora para jugar de nuevo!", SCREEN_WIDTH/2, SCREEN_HEIGHT/2.5, arcade.color.BLACK, font_size=15, anchor_x="center")

                self.game_over = True
 

    def update(self, delta_time):
        if not self.game_over and not self.showing_main_screen:
            self.snake.move()
            if self.snake.eats(self.food):
                self.food.move()
                self.score += 1

            if self.snake.segments[-1][0] < 0 or self.snake.segments[-1][0] > SCREEN_WIDTH:
                self.snake.dead = True
                print("Game over!")
            elif self.snake.segments[-1][1] < 0 or self.snake.segments[-1][1] > SCREEN_HEIGHT:
                self.snake.dead = True
                print("Game over!")


    def on_key_press(self, key, modifiers):
        if self.showing_main_screen:
            if key == arcade.key.ENTER:
                self.showing_main_screen = False
        elif self.game_over:
            if key == arcade.key.SPACE:
                self.restart_game()
        else:
            self.snake.on_key_press(key, modifiers)
    
    def restart_game(self):
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.game_over = False


def main():
    game = SnakeGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
