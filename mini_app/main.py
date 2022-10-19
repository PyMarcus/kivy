from time import sleep

from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
from kivy.app import App


class GridlayoutWidgets(GridLayout):
    change_text_when_i_click = StringProperty("Change!")
    c = 0
    counter = StringProperty(f"{c}")

    def on_click(self):
        self.change_text_when_i_click = "Changed!!!"

    def count(self):
        self.c += 1
        self.counter = f"{self.c}"


class Application(App):
    pass


if __name__ == '__main__':
    Application().run()


