import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup

class TicTacToe(GridLayout):
    def __init__(self, **kwargs):
        super(TicTacToe, self).__init__(**kwargs)

        self.cols = 3
        self.rows = 3

        self.buttons = [[Button(text='', 
                        font_size='36sp', 
                        on_press=self.on_button_click) for _ in range(3)] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                self.buttons[i][j].row = i
                self.buttons[i][j].col = j
                self.add_widget(self.buttons[i][j])

        self.turn_count = 0
        self.player_x_turn = True

    def on_button_click(self, button):
        if button.text:
            return

        player = 'X' if self.player_x_turn else 'O'
        button.text = player
        self.turn_count += 1

        if self.check_win_improved(button.row, button.col):
            self.show_message(f'Player {player} wins!')
            self.reset_game()
        elif self.turn_count == 9:
            self.show_message("It's a draw!")
            self.reset_game()

        self.player_x_turn = not self.player_x_turn

    def check_win(self, row, col):
        player = 'X' if self.player_x_turn else 'O'

        # Check row
        for i in range(3):
            if self.buttons[row][i].text != player:
                break
            if i == 2:
                return True

        # Check column
        for i in range(3):
            if self.buttons[i][col].text != player:
                break
            if i == 2:
                return True

        # Check diagonal
        if row == col:
            for i in range(3):
                if self.buttons[i][i].text != player:
                    break
                if i == 2:
                    return True

        # Check anti-diagonal
        if row + col == 2:
            for i in range(3):
                if self.buttons[i][2-i].text != player:
                    break
                if i == 2:
                    return True

        return False

    def check_win_improved(self, row, col):
        player = 'X' if self.player_x_turn else 'O'

        # Check row
        if all(self.buttons[row][i].text == player for i in range(3)):
            return True

        # Check column
        if all(self.buttons[i][col].text == player for i in range(3)):
            return True

        # Check diagonal
        if row == col and all(self.buttons[i][i].text == player for i in range(3)):
            return True

        # Check anti-diagonal
        if row + col == 2 and all(self.buttons[i][2-i].text == player for i in range(3)):
            return True

        return False

    def show_message(self, message):
        self.popup = Popup(title=message, size_hint=(None, None), size=(200, 100))
        self.popup.open()

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].text = ''
        self.turn_count = 0
        self.player_x_turn = True

class TicTacToeApp(App):
    def build(self):
        return TicTacToe()

if __name__ == '__main__':
    TicTacToeApp().run()
