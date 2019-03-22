import arcade

from models import Game
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500


class MainScreenWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BLACK)

        self.game = Game(width, height)

    def on_draw(self):
        arcade.start_render()

        arcade.draw_text(self.game.startButton, (self.width/2)-10, self.height/2, arcade.color.WHITE)



if __name__== '__main__':
    window = MainScreenWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()