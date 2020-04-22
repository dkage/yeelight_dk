import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout


class ButtonDiscover(Button):
    def __init__(self, **kwargs):
        super(ButtonDiscover, self).__init__(**kwargs)
        self.text = 'Submit'
        self.on_press = self.clicked(self)

    @staticmethod
    def clicked(self):
        print("Clicked!!!")


class AppGrid(GridLayout):

    def __init__(self, **kwargs):
        super(AppGrid, self).__init__(**kwargs)

        self.inside = GridLayout()
        self.inside.cols = 2

        button = ButtonDiscover()
        self.inside.add_widget(button)


class LightApp(App):

    def build(self):
        return AppGrid()
