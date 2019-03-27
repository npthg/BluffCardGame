import arcade
from random import randint

PLAYER_ROUND = 0

class Player:
    def __init__(self, game, playername):
        self.game = game
        self.playerName = playername

        self.point = 100

    #def updatePoint(self):
    #    self.point+=10

class Card:
    def __init__(self, game, x, y):
        self.game = game
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

    def get_CardType(self):
        return self.cardType

    def card_disappear(self):
        self.x = self.game.width
        self.y = self.game.height

class Label:
    def __init__(self, game, x, y, name):
        self.game = game
        self.x = x
        self.y = y
        self.name = name
        self.pressed = False

    def label_disappear(self):
        self.x = self.game.width
        self.y = self.game.height

    def on_press(self):
        self.pressed = True
    def on_release(self):
        self.pressed = False

class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.startButton = Label(self, 200, 250, 'Start')
        self.player_one_label = Label(self, 10, 480, 'Player1')
        self.player_two_label = Label(self, 10, 480, 'Player2')
        self.next_label = Label(self, 360, 20, 'Next')

        self.card = Card(self, 200, 250)

        self.player_one = Player(self, 1)
        self.player_two = Player(self, 2)

    def on_mouse_press(self, button, modifiers):
        if(button == arcade.MOUSE_BUTTON_LEFT):
            self.startButton.label_disappear()
            self.startButton.pressed = True