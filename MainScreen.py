import arcade

from models import Game
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500

class MainScreenWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BLACK)

        self.game = Game(width, height)

        self.card = self.game.card
        self.cardSprite = arcade.Sprite(self.card.cardImage())
        self.cardSprite.center_x = self.card.x
        self.cardSprite.center_y = self.card.y

    def on_draw(self):
        arcade.start_render()
        arcade.draw_text(self.game.startButton.name, self.game.startButton.x, self.game.startButton.y, arcade.color.WHITE)
        if(self.game.startButton.pressed):
            self.cardSprite.draw()
            arcade.draw_text(self.game.player_one_label.name, self.game.player_one_label.x, self.game.player_one_label.y,
                             arcade.color.WHITE)
            arcade.draw_text(self.game.next_label.name, self.game.next_label.x, self.game.next_label.y,
                             arcade.color.WHITE)
            arcade.draw_text('Point: '+str(self.game.player_one.point), 320, 480,
                             arcade.color.WHITE)

    def on_mouse_press(self, x, y, button, modifiers):
        self.game.on_mouse_press(button, modifiers)

if __name__== '__main__':
    window = MainScreenWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()