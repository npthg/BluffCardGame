import arcade
from models import Card, Player, Button, Label
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 500
GAME_RUNNING = 0
GAME_OVER = 1

def check_mouse_press_for_buttons(x, y, button_list):
    """ Given an x, y, see if we need to register any button clicks. """
    for button in button_list:
        if x > button.center_x + button.width / 2:
            continue
        if x < button.center_x - button.width / 2:
            continue
        if y > button.center_y + button.height / 2:
            continue
        if y < button.center_y - button.height / 2:
            continue
        button.on_press()


def check_mouse_release_for_buttons(x,y, button_list):
    """ If a mouse button has been released, see if we need to process
        any release events. """
    for button in button_list:
        if button.pressed:
            button.on_release()


class InitialButton(Button):

    def __init__(self, center_x, center_y,text, action_function):
        super().__init__(center_x, center_y, 60, 30, text, 12, "Arial")
        self.action_function = action_function

    def on_release(self):
        super().on_release()
        self.action_function()


class MainScreenWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.BLACK)

        self.player_one = Player('Player 1', 100)
        self.player_two = Player('Player 2', 100)

    def setup(self):
        print('setup')
        self.button_list = []
        self.card_button_list = []
        self.point_button_list = []
        self.truth_bluff_button_list = []
        self.continue_button_list = []

        self.start = False
        self.true_card = False
        self.next_player = False
        self.click_truth_bluff = False
        self.click_continue = False

        self.select_card = 0
        self.select_card_name = ''

        self.player_select_point = 0
        self.card = Card(self.width / 2, self.height / 2)
        self.cardSprite = arcade.Sprite(self.card.cardImage())


        self.player_one_name_label = Label(self.player_one.playerName, 20, 480)
        self.player_two_name_label = Label(self.player_two.playerName, 20, 480)

        self.card_and_point_label = Label
        self.player_one_result_label = Label
        self.player_two_result_label = Label

        self.result = ''

        self.cardSprite.center_x = self.card.x
        self.cardSprite.center_y = self.card.y

        start_button = InitialButton(self.width/2, self.height/2, 'Start', self.start_game)
        self.button_list.append(start_button)

        cat_button = InitialButton(100, 80, 'Dog', self.select_dog_card)
        dog_button = InitialButton(170, 80, 'Cat', self.select_cat_card)
        pig_button = InitialButton(240, 80, 'Pig', self.select_pig_card)
        rat_button = InitialButton(310, 80, 'Rat', self.select_rat_card)
        self.card_button_list.append(cat_button)
        self.card_button_list.append(dog_button)
        self.card_button_list.append(pig_button)
        self.card_button_list.append(rat_button)

        twentyfive_point_button = InitialButton(100, 40, '25', self.select_twentyfive_point)
        fifty_point_button = InitialButton(170, 40, '50', self.select_fifty_point)
        seventyfive_point_button = InitialButton(240, 40, '75', self.select_seventyfive_point)
        hundred_point_button = InitialButton(310, 40, '100', self.select_hundred_point)
        self.point_button_list.append(twentyfive_point_button)
        self.point_button_list.append(fifty_point_button)
        self.point_button_list.append(seventyfive_point_button)
        self.point_button_list.append(hundred_point_button)

        truth_button = InitialButton(100, self.height / 2 + 70, 'Truth', self.select_truth)
        bluff_button = InitialButton(170, self.height / 2 + 70, 'Bluff', self.select_bluff)
        self.truth_bluff_button_list.append(truth_button)
        self.truth_bluff_button_list.append(bluff_button)

        continue_button = InitialButton(self.width-100, 20, 'Continue', self.select_continue)
        self.continue_button_list.append(continue_button)

        self.current_state = GAME_RUNNING

    def draw_game(self):
        self.button_list[0].draw()
        if self.start:
            self.cardSprite.draw()
            self.player_one_name_label.draw()
            self.player_one_point_label.draw()
            for i in self.card_button_list:
                i.draw()
            for i in self.point_button_list:
                i.draw()

            if self.next_player:
                self.player_two_name_label.draw()
                self.player_two_point_label.draw()
                self.card_and_point_label.draw()
                for i in self.truth_bluff_button_list:
                    i.draw()



    def draw_gameover(self):
        arcade.draw_text(self.result, self.width / 2 - 80, self.height / 2 + 100, arcade.color.WHITE, 20)
        self.player_one_result_label.draw()
        self.player_two_result_label.draw()
        for i in self.continue_button_list:
            i.draw()

    def on_draw(self):
        arcade.start_render()
        if(self.current_state == GAME_RUNNING):
            self.draw_game()
        elif(self.current_state == GAME_OVER):
            self.draw_gameover()


    def update(self, delta):
        if self.current_state == GAME_RUNNING:
            if self.start:
                self.button_list[0].disappear()

            self.player_one_point_label = Label('Point : ' + str(self.player_one.point), 300, 480)
            self.player_two_point_label = Label('Point : ' + str(self.player_two.point), 300, 480)

            if self.card.cardType == self.select_card:
                self.true_card = True

            if self.select_card == 0:
                self.select_card_name = 'Dog Card'
            elif self.select_card == 1:
                self.select_card_name = 'Cat Card'
            elif self.select_card == 2:
                self.select_card_name = 'Pig Card'
            elif self.select_card == 3:
                self.select_card_name = 'Rat Card'

            if self.next_player:
                self.cardSprite.center_x = 1000
                self.cardSprite.center_y = 1000
                self.player_one_point_label.disappear()
                self.player_one_name_label.disappear()
                for i in self.card_button_list:
                    i.disappear()
                for i in self.point_button_list:
                    i.disappear()

                self.card_and_point_label = Label(
                    self.player_one.playerName + ' choose ' + self.select_card_name + ' and bet ' +
                    str(self.player_select_point), self.width / 2 - 110, self.height / 2 + 100)

                if self.click_truth_bluff:
                    self.current_state = GAME_OVER
                    self.player_two_point_label.disappear()
                    self.player_two_name_label.disappear()
                    self.card_and_point_label.disappear()
                    for i in self.truth_bluff_button_list:
                        i.disappear()

                self.player_one_result_label = Label(self.player_one.playerName + ' points : ' + str(self.player_one.point),
                                                 100, self.height / 2 + 70)
                self.player_two_result_label = Label(self.player_two.playerName + ' points : ' + str(self.player_two.point),
                                                 100, self.height / 2 + 50)

    def on_mouse_press(self, x, y, button, key_modifiers):
        check_mouse_press_for_buttons(x, y, self.button_list)
        check_mouse_press_for_buttons(x, y, self.card_button_list)
        check_mouse_press_for_buttons(x, y, self.point_button_list)
        check_mouse_press_for_buttons(x, y, self.truth_bluff_button_list)
        check_mouse_press_for_buttons(x, y, self.continue_button_list)
    def on_mouse_release(self, x, y, button, key_modifiers):
        check_mouse_release_for_buttons(x, y, self.button_list)
        check_mouse_release_for_buttons(x, y, self.card_button_list)
        check_mouse_release_for_buttons(x, y, self.point_button_list)
        check_mouse_release_for_buttons(x, y, self.truth_bluff_button_list)
        check_mouse_release_for_buttons(x, y, self.continue_button_list)

    def start_game(self):
        self.start = True

    def select_dog_card(self):
        self.select_card = 0

    def select_cat_card(self):
        self.select_card = 1

    def select_pig_card(self):
        self.select_card = 2

    def select_rat_card(self):
        self.select_card = 3

    def select_twentyfive_point(self):
        self.player_select_point = 25
        self.next_player = True

    def select_fifty_point(self):
        self.player_select_point = 50
        self.next_player = True

    def select_seventyfive_point(self):
        self.player_select_point = 75
        self.next_player = True

    def select_hundred_point(self):
        self.player_select_point = 100
        self.next_player = True

    def select_truth(self):
        self.click_truth_bluff = True
        if self.select_card == self.card.cardType:
            self.player_two.increase_point(self.player_select_point)
            self.player_one.decrease_point(self.player_select_point)
            self.result = 'Yes, it is truth !!'
        else:
            self.player_two.decrease_point(self.player_select_point)
            self.player_one.increase_point(self.player_select_point)
            self.result = 'No, it is bluff !!'

    def select_bluff(self):
        self.click_truth_bluff = True
        if self.select_card != self.card.cardType:
            self.player_two.increase_point(self.player_select_point)
            self.player_one.decrease_point(self.player_select_point)
            self.result = 'Yes, it is bluff !!'
        else:
            self.player_two.decrease_point(self.player_select_point)
            self.player_one.increase_point(self.player_select_point)
            self.result = 'No, it is truth !!'

    def select_continue(self):
        self.setup()


if __name__== '__main__':
    window = MainScreenWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()