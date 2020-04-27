import kivy

from kivy.app import App
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout


# Window configuration, set size and disable resize
Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '600')
Config.write()


class LightLay(FloatLayout):

    pass


class LightApp(App):
    def test(self):
        print('test')

    def build(self):
        return LightLay()