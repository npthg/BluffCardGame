import arcade
from random import randint

PLAYER_ROUND = 0

class Player:
    def __init__(self, playername, point):
        self.playerName = playername
        self.point = point
    def increase_point(self, player_select_point):
        self.point = self.point+player_select_point

    def decrease_point(self, player_select_point):
        self.point = self.point-player_select_point

class Card:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.cardType = randint(0, 3)

        self.imageList = ['images/dog.png', 'images/cat.png', 'images/pig.png', 'images/rat.png']

    def cardImage(self):
        image = ''
        if(self.cardType == 0):
            image = self.imageList[0]
        elif(self.cardType == 1):
            image = self.imageList[1]
        elif(self.cardType == 2):
            image = self.imageList[2]
        elif(self.cardType == 3):
            image = self.imageList[3]

        return image
    def disappear(self):
        self.x = 1000
        self.y = 1000

class Button:
    def __init__(self,
                 center_x, center_y,
                 width, height,
                 text,
                 font_size=18,
                 font_face="Arial",
                 face_color=arcade.color.LIGHT_GRAY,
                 highlight_color=arcade.color.WHITE,
                 shadow_color=arcade.color.GRAY,
                 button_height=2):
        self.center_x = center_x
        self.center_y = center_y
        self.width = width
        self.height = height
        self.text = text
        self.font_size = font_size
        self.font_face = font_face
        self.pressed = False
        self.face_color = face_color
        self.highlight_color = highlight_color
        self.shadow_color = shadow_color
        self.button_height = button_height

    def draw(self):
            """ Draw the button """
            arcade.draw_rectangle_filled(self.center_x, self.center_y, self.width,
                                         self.height, self.face_color)

            if not self.pressed:
                color = self.shadow_color
            else:
                color = self.highlight_color

            # Bottom horizontal
            arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                             self.center_x + self.width / 2, self.center_y - self.height / 2,
                             color, self.button_height)

            # Right vertical
            arcade.draw_line(self.center_x + self.width / 2, self.center_y - self.height / 2,
                             self.center_x + self.width / 2, self.center_y + self.height / 2,
                             color, self.button_height)

            if not self.pressed:
                color = self.highlight_color
            else:
                color = self.shadow_color

            # Top horizontal
            arcade.draw_line(self.center_x - self.width / 2, self.center_y + self.height / 2,
                             self.center_x + self.width / 2, self.center_y + self.height / 2,
                             color, self.button_height)

            # Left vertical
            arcade.draw_line(self.center_x - self.width / 2, self.center_y - self.height / 2,
                             self.center_x - self.width / 2, self.center_y + self.height / 2,
                             color, self.button_height)

            x = self.center_x
            y = self.center_y
            if not self.pressed:
                x -= self.button_height
                y += self.button_height

            arcade.draw_text(self.text, x, y,
                             arcade.color.BLACK, font_size=self.font_size,
                             width=self.width, align="center",
                             anchor_x="center", anchor_y="center")

    def on_press(self):
            self.pressed = True

    def on_release(self):
            self.pressed = False

    def disappear(self):
            self.center_x = 1000
            self.center_y = 1000

class Label:
    def __init__(self, text, center_x, center_y):
        self.center_x = center_x
        self.center_y = center_y
        self.text = text

    def draw(self):
        arcade.draw_text(str(self.text), self.center_x, self.center_y, arcade.color.WHITE)

    def disappear(self):
        self.center_x = 1000
        self.center_y = 1000